let isDraggingPopup1 = false;
let isDraggingPopup2 = false;
let offsetX1, offsetY1, offsetX2, offsetY2;

let popup1 = document.querySelector(".vizov-window");
let popup2 = document.querySelector(".video-window");

document.querySelector(".vizov").addEventListener("click", () => {
  popup1.style.display = "flex";
});

document.querySelector("#closeButton").addEventListener("click", () => {
  popup1.style.display = "none";
});

popup1.addEventListener("mousedown", (e) => {
  isDraggingPopup1 = true;
  offsetX1 = e.clientX - popup1.offsetLeft;
  offsetY1 = e.clientY - popup1.offsetTop;
  popup1.style.cursor = "grabbing";
});

document.addEventListener("mouseup", () => {
  isDraggingPopup1 = false;
  popup1.style.cursor = "grab";
});

document.addEventListener("mousemove", (e) => {
  if (!isDraggingPopup1) return;

  const x = e.clientX - offsetX1;
  const y = e.clientY - offsetY1;

  popup1.style.left = x + "px";
  popup1.style.top = y + "px";
});

document.querySelector(".videos").addEventListener("click", () => {
  popup2.style.display = "flex";
});

document.querySelector("#closeButton1").addEventListener("click", () => {
  popup2.style.display = "none";
});

popup2.addEventListener("mousedown", (e) => {
  isDraggingPopup2 = true;
  offsetX2 = e.clientX - popup2.offsetLeft;
  offsetY2 = e.clientY - popup2.offsetTop;
  popup2.style.cursor = "grabbing";
});

document.addEventListener("mouseup", () => {
  isDraggingPopup2 = false;
  popup2.style.cursor = "grab";
});

document.addEventListener("mousemove", (e) => {
  if (!isDraggingPopup2) return;

  const x = e.clientX - offsetX2;
  const y = e.clientY - offsetY2;

  popup2.style.left = x + "px";
  popup2.style.top = y + "px";
});
const callButton = document.getElementById('callButton');
const localVideo = document.getElementById('localVideo');
const hangupButton=document.getElementById('hangupButton')
callButton.addEventListener('click', async () => {
  try {
    const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true})
    
    localVideo.srcObject = stream;
    hangupButton.disabled = false;
  } catch (error) {
    console.error('Ошибка при получении доступа к камере:', error);
    alert('Не удалось получить доступ к камере. Пожалуйста, проверьте настройки доступа.');
  }
});
hangupButton.addEventListener('click', () => {
  localVideo.srcObject = null;
})
const startButton = document.getElementById('startButton');

startButton.addEventListener('click', () => {

    callButton.disabled = false;
});