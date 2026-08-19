import CourseExperience from "./course-experience";
import dataPreview from "./generated/data-preview.json";
import progressSnapshot from "./generated/progress-snapshot.json";
import qualitySummary from "./generated/data-quality-summary.json";

export default function Home() {
  return (
    <CourseExperience
      dataPreview={dataPreview}
      progressSnapshot={progressSnapshot}
      qualitySummary={qualitySummary}
    />
  );
}
