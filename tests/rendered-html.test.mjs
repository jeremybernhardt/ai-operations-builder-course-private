import assert from "node:assert/strict";
import { readdir, readFile } from "node:fs/promises";
import test from "node:test";

const developmentPreviewMeta =
  /<meta(?=[^>]*\bname=["']codex-preview["'])(?=[^>]*\bcontent=["']development["'])[^>]*>/i;

async function renderHome() {
  const workerUrl = new URL("../dist/server/index.js", import.meta.url);
  workerUrl.searchParams.set("test", `${process.pid}-${Date.now()}`);
  const { default: worker } = await import(workerUrl.href);
  const response = await worker.fetch(
    new Request("http://localhost/", { headers: { accept: "text/html" } }),
    { ASSETS: { fetch: async () => new Response("Not found", { status: 404 }) } },
    { waitUntil() {}, passThroughOnException() {} },
  );
  return { response, html: await response.text() };
}

test("renders development preview metadata", async () => {
  const { response, html } = await renderHome();
  assert.equal(response.status, 200);
  assert.match(response.headers.get("content-type") ?? "", /^text\/html\b/i);
  assert.match(html, developmentPreviewMeta);
});

test("renders the required course areas and current checkpoint", async () => {
  const { response, html } = await renderHome();
  assert.equal(response.status, 200);
  assert.match(html, /Course Portal/);
  assert.match(html, /KPI Lab/);
  assert.match(html, /M0\.5-C2/);
  assert.match(html, /Builder plan review verified/);
  assert.match(html, /Read-only mirror/);
  assert.match(html, /Course progress/);
  assert.match(html, /Learning objectives/);
  assert.match(html, /Course artifacts/);
  assert.match(html, /Capability evidence/);
  assert.match(html, /One lesson per task/);
  assert.doesNotMatch(html, /Working glossary/);
  assert.doesNotMatch(html, /accepted_first_pass_count/);
  assert.doesNotMatch(html, /0\.583333/);

  const assetsDirectory = new URL("../dist/client/assets/", import.meta.url);
  const assetNames = await readdir(assetsDirectory);
  const courseAsset = assetNames.find((name) => name.startsWith("course-experience-") && name.endsWith(".js"));
  assert.ok(courseAsset, "course experience client asset was not built");
  const clientCode = await readFile(new URL(courseAsset, assetsDirectory), "utf8");
  assert.match(clientCode, /What counts as a first pass/);
  assert.match(clientCode, /The situation/);
  assert.match(clientCode, /Duplicate example/);
  assert.match(clientCode, /Review the counting rules you chose/);
  assert.match(clientCode, /Copy result/);
  assert.match(clientCode, /localStorage/);
  assert.match(clientCode, /Stored only|stay only in this browser|Autosaved only/);
  assert.match(clientCode, /Reset review workspace/);
  assert.match(clientCode, /Step 5 · Lesson closeout/);
  assert.match(clientCode, /Continue in a new conversation/);
  assert.match(clientCode, /SESSION_HANDOFF\.md/);
  assert.match(clientCode, /NEXT_CHAT_PROMPT\.md/);
  assert.match(clientCode, /GitHub continuity is active/);
  assert.match(clientCode, /Private GitHub repository/);
  assert.match(clientCode, /M0\.5-L3: Reviewing an AI-generated diff and verification evidence/);
  assert.match(clientCode, /Optional specialization/);
  assert.doesNotMatch(clientCode, /AfterQuery/);
  assert.doesNotMatch(clientCode, /Copy draft for chat/);
  assert.doesNotMatch(clientCode, /accepted_first_pass_count/);
  assert.doesNotMatch(clientCode, /0\.583333/);
});
