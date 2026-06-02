<template>
  <div class="page">

    <main class="content">

      <!-- HERO -->
      <section class="hero">

        <div class="hero-content">
          <h1>BASKETSHOES</h1>

          <p>
            Las mejores zapatillas de básquet, estilo y rendimiento en un solo lugar.
          </p>

          <div class="hero-buttons">
            <button class="btn-primary">Comprar Ahora</button>
            <button class="btn-secondary">Ver Productos</button>
          </div>
        </div>

        <div class="hero-image">
          <img
            src="https://wp.theringer.com/wp-content/uploads/2026/05/cropped-WembyTakesGame7_Getty-Ringer-scaled-1.jpg"
            alt="Victor Wembanyama"
          />
        </div>

      </section>

      <!-- PRODUCTOS -->
      <section class="shoes-section">
        <h2>Zapatillas Destacadas</h2>

        <div class="shoes-grid">

          <div class="product-card">
            <button class="shoe-button">
              <img
                src="https://images.stockx.com/images/Nike-Kobe-6-Protro-Reverse-Grinch.jpg"
                alt="Nike Kobe 6"
              />
            </button>
            <h3>Nike Kobe 6 Protro</h3>
            <p class="price">$289.999</p>
            <button class="buy-btn">Comprar</button>
          </div>

          <div class="product-card">
            <button class="shoe-button">
              <img
                src="https://images.stockx.com/images/361-Degrees-Joker-1-Joker.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2"
                alt="361 Joker"
              />
            </button>
            <h3>361° Joker 1</h3>
            <p class="price">$219.999</p>
            <button class="buy-btn">Comprar</button>
          </div>

          <div class="product-card">
            <button class="shoe-button">
              <img
                src="https://images.stockx.com/images/Nike-LeBron-21-Tahitian.jpg"
                alt="LeBron 21"
              />
            </button>
            <h3>Nike LeBron 21</h3>
            <p class="price">$259.999</p>
            <button class="buy-btn">Comprar</button>
          </div>

          <div class="product-card">
            <button class="shoe-button">
              <img
                src="https://images.stockx.com/images/Nike-Zoom-GT-Cut-3-EP-Black-White-Iron-Grey.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1729711200"
                alt="GT Cut 3"
              />
            </button>
            <h3>Nike GT Cut 3</h3>
            <p class="price">$239.999</p>
            <button class="buy-btn">Comprar</button>
          </div>

        </div>
      </section>

      <!-- BENEFICIOS -->
      <section class="features-section">
        <h2>¿Por qué elegir BasketShoes?</h2>

        <div class="features-grid">

          <div class="feature-card">
            <h3>🚚 Envíos</h3>
            <p>Realizamos envíos a todo el país.</p>
          </div>

          <div class="feature-card">
            <h3>💳 Cuotas</h3>
            <p>Hasta 12 cuotas sin interés.</p>
          </div>

          <div class="feature-card">
            <h3>⭐ Originales</h3>
            <p>Productos 100% originales.</p>
          </div>

          <div class="feature-card">
            <h3>🔄 Cambios</h3>
            <p>30 días para cambios y devoluciones.</p>
          </div>

        </div>
      </section>

      
    </main>

    <Footer />

  </div>
</template>

<script>
import Footer from "./components/Footer.vue";

export default {
  name: "App",
  components: {
    Footer,
  },
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Barlow:wght@300;400;500;600;700;900&display=swap');

:root {
  --orange: #FF6B00;
  --black: #0A0A0A;
  --white: #F5F5F5;
}

body {
  margin: 0;
  font-family: 'Barlow', sans-serif;
  background: var(--black);
  color: var(--white);
}

.page {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background:
    linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.95)),
    url("https://wallpapercave.com/wp/wp7547008.jpg")
    center/cover no-repeat;
}

.content {
  flex: 1;
}

/* HERO */

.hero {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 40px;
  gap: 40px;
  flex-wrap: wrap;
}

.hero-content {
  max-width: 600px;
}

.hero h1 {
  font-family: 'Bebas Neue', sans-serif;
  font-size: clamp(3rem, 8vw, 7rem);
  color: var(--orange);
}

.hero p {
  font-size: 1.2rem;
  color: #ccc;
}

.hero-buttons {
  margin-top: 30px;
  display: flex;
  gap: 15px;
}

.btn-primary,
.btn-secondary,
.buy-btn {
  cursor: pointer;
  border: none;
  padding: 14px 24px;
  border-radius: 10px;
  font-weight: bold;
  transition: .3s;
}

.btn-primary,
.buy-btn {
  background: var(--orange);
  color: white;
}

.btn-secondary {
  background: transparent;
  border: 2px solid var(--orange);
  color: var(--orange);
}

.btn-primary:hover,
.buy-btn:hover {
  transform: translateY(-3px);
}

.hero-image img {
  width: 700px;
  max-width: 100%;
  border-radius: 15px;
  box-shadow: 0 0 30px rgba(255,107,0,.5);
}

/* PRODUCTOS */

.shoes-section {
  padding: 80px 40px;
  text-align: center;
}

.shoes-section h2,
.features-section h2,
.video-section h2 {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 3rem;
  color: var(--orange);
  margin-bottom: 40px;
}

.shoes-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(300px,1fr));
  gap: 30px;
}

.product-card {
  background: rgba(255,255,255,0.05);
  border: 1px solid rgba(255,107,0,.2);
  border-radius: 15px;
  padding: 20px;
}

.shoe-button {
  background: transparent;
  border: none;
  padding: 0;
}

.shoe-button img {
  width: 100%;
  height: 240px;
  object-fit: cover;
  border-radius: 10px;
}

.price {
  color: var(--orange);
  font-size: 1.4rem;
  font-weight: bold;
}

/* BENEFICIOS */

.features-section {
  padding: 80px 40px;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(250px,1fr));
  gap: 25px;
}

.feature-card {
  background: rgba(255,255,255,.05);
  border: 1px solid rgba(255,107,0,.2);
  border-radius: 15px;
  padding: 25px;
  text-align: center;
}

.feature-card h3 {
  color: var(--orange);
}

/* VIDEO */

.video-section {
  padding: 80px 40px;
  text-align: center;
}

.video-container {
  display: flex;
  justify-content: center;
}

.video-container iframe {
  width: 900px;
  max-width: 100%;
  height: 500px;
  border: none;
  border-radius: 20px;
  box-shadow: 0 0 30px rgba(255,107,0,.4);
}

/* RESPONSIVE */

@media (max-width: 900px) {
  .hero {
    text-align: center;
    justify-content: center;
  }

  .hero-buttons {
    justify-content: center;
  }
}
</style>