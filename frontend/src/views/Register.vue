<template>
    <div class = "register-container">
        <v-sheet :elevation="24" rounded class = "register-title">
            <h2> Register </h2>
        </v-sheet>
        <v-sheet :elevation="24" rounded class = "register-sheet">
            <v-form @submit.prevent>
                <v-text-field
                    v-model="userName"
                    :rules="[value => required(value, 'User Name')]"
                    label="User Name"
                ></v-text-field>
                <v-text-field
                    v-model="password"
                    :rules="[value => required(value, 'Password')]"
                    label="Password"
                ></v-text-field>
                <v-text-field
                    v-model="mail"
                    :rules="[value => required(value, 'Email')]"
                    label="Email Address"
                ></v-text-field>
                <v-btn class="mt-2" type="submit" block v-on:click="userRegister()">Submit</v-btn>
            </v-form>
        </v-sheet>
    </div>
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
        required(value, fieldName) {
        if (value) return true;
        return `You must enter a ${fieldName}.`;
        },
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

<style scoped>
  .register-container {
    display: grid;
    place-items: center;
    height: 50vh;
  }
  .register-title{
    height: 5vh;
    width: 10vw;
    display: grid;
    place-items: center;
    background-color: rgba(240, 248, 255, 0.226);
    color: rgb(16, 26, 2)
  }
  .register-sheet{
    height: 40vh;
    width: 20vw;
    background-color: rgba(240, 248, 255, 0.84);
    padding: 20px; 
  }
</style>
