<template>
  <!-- Este componente no renderiza nada visible -->
  <div></div>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Barlow:wght@300;400;500;600;700;900&display=swap');

:root {
  --orange: #FF6B00;
  --black: #0A0A0A;
  --white: #F5F5F5;
}

/* ===== RESET ===== */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Barlow', sans-serif;
  background: var(--black);
  color: var(--white);
  overflow-x: hidden;
}

/* ===== PAGE ===== */
.page {
  min-height: 100vh;
  display: flex;
  flex-direction: column;

  background:
    linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.95)),
    url("https://wallpapercave.com/wp/wp7547008.jpg");
  background-size: cover;
  background-position: center;
}

/* ===== HERO ===== */
.hero {
  min-height: 90vh;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 60px;
  gap: 40px;
}

/* TEXTO */
.hero h1 {
  font-family: 'Bebas Neue', sans-serif;
  font-size: clamp(3rem, 8vw, 7rem);
  color: var(--orange);
  letter-spacing: 3px;
}

.hero p {
  margin-top: 20px;
  color: #ccc;
  font-size: 1.2rem;
  max-width: 500px;
}

/* BOTONES */
button {
  cursor: pointer;
  border: none;
  padding: 14px 24px;
  border-radius: 10px;
  font-weight: bold;
  transition: 0.3s ease;
}

.btn-primary {
  background: var(--orange);
  color: white;
}

.btn-primary:hover {
  transform: translateY(-3px);
  box-shadow: 0 0 25px rgba(255, 107, 0, 0.5);
}

.btn-secondary {
  background: transparent;
  border: 2px solid var(--orange);
  color: var(--orange);
}

.btn-secondary:hover {
  background: rgba(255, 107, 0, 0.1);
}

/* ===== IMÁGENES ===== */
.hero-image img {
  width: 420px;
  border-radius: 20px;
  box-shadow: 0 0 35px rgba(255, 107, 0, 0.4);
  transition: 0.3s ease;
}

.hero-image img:hover {
  transform: scale(1.05);
}

/* ===== PRODUCTOS ===== */
.products {
  padding: 60px;
}

.products h2 {
  font-family: 'Bebas Neue', sans-serif;
  color: var(--orange);
  font-size: 3rem;
  margin-bottom: 30px;
}

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 25px;
}

.card {
  background: rgba(20,20,20,0.9);
  border: 1px solid rgba(255,107,0,0.3);
  border-radius: 15px;
  overflow: hidden;
  transition: 0.3s ease;
}

.card:hover {
  transform: translateY(-8px);
  border-color: var(--orange);
  box-shadow: 0 0 30px rgba(255, 107, 0, 0.3);
}

.card img {
  width: 100%;
  height: 220px;
  object-fit: cover;
}

.card h3 {
  padding: 15px;
  color: var(--orange);
}

.card p {
  padding: 0 15px 15px;
  color: #bbb;
}
</style>