importScripts("https://www.gstatic.com/firebasejs/9.12.1/firebase-app-compat.js")
importScripts("https://www.gstatic.com/firebasejs/9.12.1/firebase-messaging-compat.js")

firebase.initializeApp({
    apiKey: "AIzaSyDBYbMrnvrRZiV1McbHZM5MSkGlrYZfc-0",
    authDomain: "fast-delivery-ae47f.firebaseapp.com",
    projectId: "fast-delivery-ae47f",
    storageBucket: "fast-delivery-ae47f",
    messagingSenderId: "57531189647",
    appId: "1:57531189647:web:4b2c775d0f29e0796b63fa"
});

const messaging = firebase.messaging();