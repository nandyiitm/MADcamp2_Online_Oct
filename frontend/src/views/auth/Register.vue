<template>
    <h1>Create account to dive in</h1>

    <form @submit.prevent="createAccount">
        <p>{{ username }} | {{ password }} | {{ confirmPassword }}</p>
        <input v-model="username" type="text" placeholder="Username" required/>
        <input v-model="password" type="password" placeholder="Password" required/>
        <input v-model="confirmPassword" type="password" placeholder="Confirm Password" required/>
        <button type="submit">Register</button>
    </form>

    <div id="msg">{{ message }}</div>

</template>

<script setup>
import { ref } from 'vue';
import router from '@/router';

const username = ref('');
const password = ref('');
const confirmPassword = ref('');
const message = ref('');


function createAccount() {
    alert('creating account');
    if (password.value !== confirmPassword.value) {
        message.value = "Passwords do not match!";
        return;
    }

    fetch('http://127.0.0.1:5000/register', {
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
                if (response.status === 401) {
                    router.push('/login');
                    throw new Error('Unauthorized: Please log in to access this resource.');
                }
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
            router.push('/login');
        })
        .catch(error => {
            console.error('Error fetching message:', error);
            message.value = 'Error fetching message';
        });
}

</script>