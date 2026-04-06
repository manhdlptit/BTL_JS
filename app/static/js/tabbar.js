function openTab(name) {
  let i = 0;
  let x = document.getElementsByClassName("tabbar");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  document.getElementById(name).style.display = "block";
}
