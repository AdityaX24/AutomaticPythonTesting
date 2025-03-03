export const uploadScript = async (formData: FormData) => {
  const response = await fetch("http://127.0.0.1:8000/upload/script", {
    // Update the endpoint to match the backend
    method: "POST",
    body: formData,
  });
  return response.json();
};

export const uploadTestCase = async (formData: FormData) => {
  const response = await fetch("http://127.0.0.1:8000/upload/testcase", {
    method: "POST",
    body: formData,
  });
  return response.json();
};

export const deleteScripts = async (path: string) => {
  console.log(path);
  const response = await fetch("http://127.0.0.1:8000/delete-scripts", {
    method: "POST", // Keep as POST
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ path: path }), // Send as JSON
  });
  return response.json();
};

export const deleteTestCases = async (path: string) => {
  console.log(path);
  const response = await fetch("http://127.0.0.1:8000/delete-testcases", {
    method: "POST", // Keep as POST
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ path: path }), // Send as JSON
  });
  return response.json();
};

export const runTests = async () => {
  const response = await fetch("http://127.0.0.1:8000/run-tests", {
    method: "GET",
  });
  // Handle the response as text (CSV)
  const csvData = await response.text();
  console.log(csvData);
  return csvData;
};

export const listFiles = async () => {
  const response = await fetch("http://127.0.0.1:8000/list-files");
  return response.json();
};
