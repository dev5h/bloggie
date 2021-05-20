document.getElementById("submitBtn").onclick = (e) => {
  let fname = document.getElementById("fname");
  let uname = document.getElementById("uname");
  let pwd = document.getElementById("pwd");
  let email = document.getElementById("email");

  let STATUS = 200;
  if (
    fname.length > 0 &&
    uname.length > 0 &&
    pwd.length > 0 &&
    email.length > 0
  ) {
    alert("Great");
  }
};
var STATUS = undefined;
document.getElementById("form").addEventListener("input", () => {
  let fname = document.getElementById("fname").value;
  let uname = document.getElementById("uname").value;
  let pwd = document.getElementById("pwd").value;
  let email = document.getElementById("email").value;

  if (
    fname.length > 0 &&
    uname.length > 0 &&
    pwd.length > 0 &&
    email.length > 0
  ) {
    if (fname.length < 6) STATUS = "shrtfname";
    else if (uname.length < 4) STATUS = "shrtuname";
    else if (pwd.length < 6) STATUS = "shrtpwd";
    else STATUS = 200;
  } else {
    status = "nullVAlue";
  }
  if (STATUS == 200) {
    document.getElementById("submitBtn").removeAttribute("disabled");
  } else {
    document.getElementById("submitBtn").setAttribute("disabled", "");
    document.getElementById("error_text").innerHTML = "Oops! Something went wrong :("
  }
});

submitBtn = document.getElementById("submitBtn");
document.getElementById("submitBtn").onclick = (e) => {
  submitBtn.innerHTML = `<img src="/static/assets/spinner.svg" alt="" id="spinner-svg" />`;
  let fname = document.getElementById("fname").value;
  let uname = document.getElementById("uname").value;
  let pwd = document.getElementById("pwd").value;
  let email = document.getElementById("email").value;

  const xhr = new XMLHttpRequest();
  xhr.open("POST", "/api/validate/users/registration", true);
  xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhr.onload = () => {
    if (xhr.status == 200) {
      submitBtn.innerHTML = "Let's Go";
      const response = xhr.responseText
      if (response == "success"){
        window.location.assign("interests")
      }else {
        document.getElementById("warning-msg").style.display= "flex"

      }
    }
  };
  xhr.send(`fname=${fname}&uname=${uname}&email=${email}&pwd=${pwd}`);
};
