import HomeView from "./components/Home.vue";
import SignUp from "./components/SignUp.vue";
import LoginView from "./components/Login.vue";
import AddRest from "./components/AddRest.vue";
import UpdateRest from "./components/UpdateRest.vue";

import {createRouter, createWebHistory} from 'vue-router'


const routes = [
    {
        name: 'HomeView',
        component:HomeView,
        path: '/'
    },
        {
        name: 'SignUp',
        component:SignUp,
        path: '/signup'
    },
        {
        name: 'LoginView',
        component:LoginView,
        path: '/login'
    },
        {
        name: 'AddRest',
        component:AddRest,
        path: '/add'
    },
        {
        name: 'UpdateRest',
        component:UpdateRest,
        path: '/update/:id'
    }
]


const router = createRouter(
    {
        history: createWebHistory(),
        routes
    }
);

export default router;