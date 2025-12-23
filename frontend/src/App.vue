<template>
<router-view/>
</template>

<script>
export default {
  name: 'App',
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

html, body {
  margin: 0;
  padding: 0;
}

/* STYLE POUR signup ET login */
/* STYLE POUR signup ET login */
/* STYLE POUR signup ET login */

.logo {
    width: 250px;
}

.container {
    margin-top: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
}

.register, .login {
    background: #ffffff;
    padding: 30px;
    width: 320px;
    border-radius: 12px;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
    display: flex;
    flex-direction: column;
    gap: 15px;
}

/* Titre */
.register h2, .login h2{
    text-align: center;
    color: #333;
    margin-bottom: 10px;
}

/* Inputs */
.register input, .login input {
    padding: 12px;
    border-radius: 8px;
    border: 1px solid #ddd;
    font-size: 14px;
    transition: 0.3s ease;
}

.register input:focus, .login input:focus {
    outline: none;
    border-color: #ff914d;
    box-shadow: 0 0 6px rgba(255, 145, 77, 0.4);
}

/* Bouton */
.register button, .login button {
    padding: 12px;
    border: none;
    border-radius: 8px;
    background-color: #ff914d;
    color: white;
    font-size: 16px;
    cursor: pointer;
    transition: 0.3s ease;
}

.register button:hover, .login button:hover {
    background-color: #e67e22;
}
</style>
