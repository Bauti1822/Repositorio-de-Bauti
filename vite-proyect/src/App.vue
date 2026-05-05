<template>
  <div class="page">
    <Navbar />
    <Footer />
  </div>
</template>

<script>
import Navbar from "./components/Navbar.vue";
import Footer from "./components/Footer.vue";

export default {
  name: "App",
  components: {
    Navbar,
    Footer,
  },
};
</script>

<style>
.page {
  min-height: 85vh;
  display: flex;
  flex-direction: column;
}

Footer {
  margin-top: auto;
}
</style>