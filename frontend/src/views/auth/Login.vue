<template>
    <h1>Login to your account to dive in</h1>

    <form @submit.prevent="createAccount">
        <p>{{ username }} | {{ password }}</p>
        <input v-model="username" type="text" placeholder="Username" required/>
        <input v-model="password" type="password" placeholder="Password" required/>
        <button type="submit">Register</button>
    </form>

    <div id="msg">{{ message }}</div>

</template>

<script setup>
import { ref } from 'vue';
import router from '@/router';

const username = ref('');
const password = ref('');
const message = ref('');


function createAccount() {
    alert('logging in account');

    fetch('http://127.0.0.1:5000/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            username: username.value,
            password: password.value
        })
    })
        .then(response => {
            if (!response.ok) {
                response.json().then(data => {
                    message.value = data.message || 'Error occurred';
                });
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log(data);
            message.value = data.message;
            localStorage.setItem('token', data.token);
            if (data.role === 'admin') {
                router.push('/admin');
            } else {
                router.push('/dashboard');
            }
        })
        .catch(error => {
            console.error('Error fetching message:', error);
            message.value = 'Error fetching message';
        });
}

</script>