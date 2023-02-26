console.log("script ran");

const userQuestionEl = document.getElementById("user-question");
const copyUserQuestion = document.getElementById("copy-user-question");
const aiResultText = document.getElementById("ai-result-text");
const submitButtonEl = document.getElementById("submit-button");
const afterQuestionTextEls = document.querySelectorAll("#after-question-text");
const sourceOneEl = document.getElementById("source-1");
const sourceTwoEl = document.getElementById("source-2");
const sourcesEl = document.getElementsByClassName("sources")[0];
const aiSectionEl = document.getElementsByClassName("ai-response")[0];

function addAIResponse(response, question) {
  aiResultText.innerText = response;
  afterQuestionTextEls.forEach((el) => (el.style.display = "block"));
  copyUserQuestion.innerText = question;
  aiSectionEl.style.display = "block";
  editSubmitButton("Submit");
}

function addSources(sources) {
  sourceOneEl.innerText = sources[0];
  sourceTwoEl.innerText = sources[1];
  sourcesEl.style.display = "block";
}

async function submitButton() {
  const userQuestion = userQuestionEl.value;
  const url = "http://127.0.0.1:5000/api/reply/";
  const testingUrl =
    "https://webhook.site/6f2636a6-abc8-41ff-a21a-8e1c9a8a681d";
  const data = {
    method: "POST",
    body: JSON.stringify({ text: userQuestion }),
    headers: {
      "Content-Type": "application/json",
    },
  };
  const response = await fetch(url, data);
  const result = await response.json();
  console.log(result);
  addAIResponse(result.response, userQuestion);
  addSources(result.sources);
}

function editSubmitButton(text, isDisabled = false) {
  submitButtonEl.innerText = text;
  submitButtonEl.disabled = isDisabled;
}

userQuestionEl.onkeydown = function (event) {
  if (event.keyCode === 13 && !event.shiftKey) {
    event.preventDefault();
    submitButton();
    editSubmitButton("Submitted ...", true);
  }
};

// const reader = response.body.getReader();

// while (true) {
//   const { value, done } = await reader.read();
//   if (done) break;
//   console.log("Received", value);
// }

// console.log("Response fully received");
