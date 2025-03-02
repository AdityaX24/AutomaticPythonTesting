export interface FileList {
    scripts: string[];
    questions: string[];
  }
  
  export interface TestCaseUploadProps {
    questionId: string;
    testType: 'input' | 'output' | 'args';
  }