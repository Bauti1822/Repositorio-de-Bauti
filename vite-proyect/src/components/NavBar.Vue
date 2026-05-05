<template>
  <div>
    <header class="page">
      <h1>BASKETSHOES</h1>
      <input type="text" placeholder="Buscar productos..." />
      <nav>
        <button>Inicio</button>
        <button>Ofertas</button>
        <button>Descuentos</button>
        <button>Ayuda</button>
        <button>Envíos</button>
      </nav>
    </header>

    <main></main>

  </div>
</template>

<script>
export default { name: "Navbar" };
</script>

<style scope>
.page { background:#222; color:#fff; padding:10px; text-align:center; }
input { padding:5px; margin:10px 0; }
nav { display:flex; flex-wrap:wrap; justify-content:center; gap:5px; }
button { padding:5px 10px; background:#444; color:#fff; border:none; }
main { flex:1; }
</style>