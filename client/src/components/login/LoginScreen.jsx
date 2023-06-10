import React, {useState} from "react";
import './LoginScreen.css'
import logo from '../../images/rioservice_logo.webp'

function closeErrorMessage(){

}

export default function LoginScreen(props) {
    const [login, setLogin] = useState(null)
    const [password, setPassword] = useState(null)
    const [errorMessage, setErrorMessage] = useState(null)

    const options = {
        headers : {'Content-Type' : 'application/json'},
        mode: "cors",
        cache: "default",
        method: 'POST',
        body: JSON.stringify({"login": login, "password": password})
    }

    const handleSendForm = (e) => {
        e.preventDefault();
        const route = 'http://localhost:5000/app/login'
        const targetUrl = `${route}`
        fetch(targetUrl, options)
        .then(request => {
            request.json().then(response => {
                if(!response.user_logged_in){
                    setErrorMessage(response.Erro)
                }
                props.setUserLoggedIn(response.user_logged_in)
            })
        })
    }

    const errorElement = <p id="error">{errorMessage}</p>

    return (<>
        <form onSubmit={handleSendForm}>
            <img className="logo_login" src={logo} alt="Logo da Rio Service"></img>
            <label htmlFor="input_login">Login</label>
            <input type="text" name="input_login" id="input_login" autoComplete="username" placeholder="Nome de usuario" onInput={(e) => {setLogin(e.target.value)}}></input>
            <label htmlFor="input_senha">Senha</label>
            <input type="password" name="input_senha" id="input_senha" autoComplete="current-password" placeholder="Senha" onInput={(e) => {setPassword(e.target.value)}}></input>
            <input type="submit" name="submit" id="submit" value="Entrar"></input>
            {errorElement}
            <p className="versao">{props.version}</p>
        </form>
    </>
    )
}