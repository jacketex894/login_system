<template>
    <div>
        <h2> Register </h2>
        <div>
            <label> UserName </label>
            <input v-model="userName"/>
        </div>
        <div>
            <label> Password </label>
            <input v-model="password"/>
        </div> 
        <div>
            <label> Email Address </label>
            <input v-model="mail"/>
        </div> 
    </div>
    <button v-on:click="userRegister()"> Register </button>
</template>
<script>
import {register} from '@/utils/userDB.js'
export default {
    name: 'Register',
    data(){
        return{
            userName:null,
            mail:null,
            password:null,
        };
    },
    methods:{
        userRegister(){
            let userData = {
                'user_name':this.userName,
                'mail':this.mail,
                'password':this.password
            };
            register(userData);
        }
    }
}
</script>