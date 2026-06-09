<template>
  <div class="productos-container">

    <section class="categoria">
      <h2>Nuevos Lanzamientos</h2>

      <div class="productos-grid">
        <div class="card">
          <img src="https://hoopshoes.net/wp-content/uploads/2026/05/1-18.webp">
          <h3>Nike LeBron 22</h3>
          <p>$249.999</p>
        </div>

        <div class="card">
          <img src="https://hoopshoes.net/wp-content/uploads/2025/11/6.png">
          <h3>Jordan Tatum 3</h3>
          <p>$219.999</p>
        </div>

        <div class="card">
          <img src="https://hoopshoes.net/wp-content/uploads/2026/03/1-12.webp">
          <h3>Nike KD 18</h3>
          <p>$239.999</p>
        </div>
      </div>
    </section>

    <section class="categoria">
      <h2>Más Vendidas</h2>

      <div class="productos-grid">
        <div class="card">
          <img src="https://cdn-images.farfetch-contents.com/29/65/21/76/29652176_58932455_600.jpg">
          <h3>Ja 2</h3>
          <p>$199.999</p>
        </div>

        <div class="card">
          <img src="https://www.underarmour.com.ar/on/demandware.static/-/Sites-underarmour_staging/default/dw9a15298c/new_images/3027630-001/IMAGE-1.jpeg">
          <h3>Curry 12</h3>
          <p>$214.999</p>
        </div>

        <div class="card">
          <img src="https://ricoseller.net/cdn/shop/files/ADIDAS-HARDEN-VOL.9-CORE-BLACK-RICOSELLER.NET.jpg?v=1757342817"
        >
          <h3>Harden Vol. 9</h3>
          <p>$229.999</p>
        </div>
      </div>
    </section>

    <section class="categoria">
      <h2>Ofertas</h2>

      <div class="productos-grid">
        <div class="card">
          <img src="https://cdn-images.farfetch-contents.com/22/99/62/16/22996216_59601518_600.jpg">
          <h3>Puma MB.03</h3>
          <p>$149.999</p>
        </div>

        <div class="card">
          <img src="https://www.moov.com.ar/on/demandware.static/-/Sites-365-dabra-catalog/default/dwde42033a/products/ADJI1939/ADJI1939-1.JPG">
          <h3>Adidas Dame 9</h3>
          <p>$159.999</p>
        </div>

        <div class="card">
          <img src="https://media-www.sportchek.ca/product/div-05-footwear/dpt-80-footwear/sdpt-01-mens/334460331/nike-unisex-precision-7-black-gold-225-u-31a0a133-6fd7-4317-a261-6679f51420e0-jpgrendition.jpg">
          <h3>Nike Precision</h3>
          <p>$129.999</p>
        </div>
      </div>
    </section>

  </div>
</template>

<style scoped>
.productos-container {
  min-height: 100vh;
  background: #0a0a0a;
  color: white;
  padding: 50px;
}

.categoria {
  margin-bottom: 70px;
}

.categoria h2 {
  text-align: center;
  color: #ff6b00;
  font-size: 2.8rem;
  margin-bottom: 40px;
  text-transform: uppercase;
  letter-spacing: 2px;
}

.categoria h2::after {
  content: "";
  display: block;
  width: 120px;
  height: 4px;
  background: #ff6b00;
  margin: 12px auto 0;
  border-radius: 10px;
}

.productos-grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 30px;
}

.card {
  width: 300px;
  background: #ffffff;
  border: 2px solid #ff6b00;
  border-radius: 18px;
  overflow: hidden;
  text-align: center;
  transition: 0.3s;
}

.card:hover {
  transform: translateY(-8px);
  box-shadow: 0 0 25px rgba(255, 107, 0, 0.5);
}

.card img {
  width: 100%;
  height: 240px;
  object-fit: cover;
}

.card h3 {
  color: #111;
  margin: 15px 10px;
}

.card p {
  color: #ff6b00;
  font-size: 1.4rem;
  font-weight: bold;
  margin-bottom: 20px;
}

.card button {
  background: #ff6b00;
  color: white;
  border: none;
  padding: 12px 20px;
  margin-bottom: 20px;
  border-radius: 10px;
  cursor: pointer;
  font-weight: bold;
}

.card button:hover {
  background: #e65f00;
}
</style>