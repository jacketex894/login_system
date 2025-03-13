const BASE_URL = 'http://127.0.0.1:8000';

export function login(account,password){
    let data = {'account':account,'password':password}
    return fetch(`${BASE_URL}/login`,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
        },
        body:JSON.stringify(data)
    }).then(response =>{
        return response.json();
    })
}
