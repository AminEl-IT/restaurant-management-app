<template>
    <header class="header-wrapper">
        <!-- LOGO (en dehors de la couleur) -->
        <div class="logo-box">
            <img src="../assets/resto-amin.png" alt="Logo" />
        </div>

        <!-- NAV COLORÉ -->
        <div class="header">
            <nav class="nav">
                <router-link to="/" class="nav-link">Home</router-link>
                <router-link to="/add" class="nav-link">Add Restaurant</router-link>
                <a href="#" class="nav-link logout" @click.prevent="logout">Logout</a>
            </nav>
        </div>
    </header>
</template>

<script>
export default {
    name: 'HeaderView',

    methods: {
        logout() {
            localStorage.removeItem('user-info')
            this.$router.push('/login')
        }
    }
}
</script>

<style>
/* Wrapper global */
.header-wrapper {
    display: flex;
    align-items: stretch;
    /* même hauteur */
}

/* Logo hors couleur */
.logo-box {
    background-color: #ffffff;
    padding: 0 25px;
    display: flex;
    align-items: center;
    box-shadow: 4px 0 10px rgba(0, 0, 0, 0.1);
}

.logo-box img {
    height: 60px;
    width: auto;
}

/* Header coloré */
.header {
    flex: 1;
    display: flex;
    align-items: center;
    padding: 15px 30px;
    background: linear-gradient(135deg, #ff914d, #4caf50);
}

/* Navigation */
.nav {
    display: flex;
    gap: 20px;
    margin-left: auto;
}

.nav-link {
    text-decoration: none;
    color: white;
    font-weight: 500;
    padding: 8px 14px;
    border-radius: 6px;
    transition: 0.3s ease;
}

.nav-link:hover {
    background-color: rgba(255, 255, 255, 0.2);
}

.router-link-active {
    background-color: rgba(255, 255, 255, 0.3);
}

/* Logout */
.logout {
    background-color: #e74c3c;
    font-weight: bold;
}

.logout:hover {
    background-color: #c0392b;
}
</style>