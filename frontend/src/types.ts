export interface FileList {
  scripts: string[];
  questions: Record<string, string[]>; // Object with question IDs as keys
}

export interface TestCaseUploadProps {
  questionId: string;
  testType: "input" | "output" | "args";
}
