import React, {useState} from "react";
import LoginScreen from "./components/login/LoginScreen";
import Dashboard from "./components/dashboard/Dashboard";

export default function DataLayer(props) {
    const [apiName, setApiName] = useState(null)
    const [apiVersion, setApiVersion] = useState(null)
    const [currentRoute, setCurrentRoute] = useState("/login")
    const [isUserLoggedIn, setUserLoggedIn] = useState(false)
    const options = {
        headers : {
            'Content-Type' : 'application/json'
        },
        mode: "cors",
        cache: "default",
        method : 'GET'
    }

    const route = '/app/data'
    const targetUrl = `${route}`

    const getAppData = () => {
        fetch(targetUrl, options)
        .then( response => {
            if(response.ok){
                response.json().then( response => {
                const {api_name, api_version} = response
                setApiName(api_name)
                setApiVersion(api_version)
            } )
          }
        })
    }

    getAppData()

    return (
        <>
            {isUserLoggedIn ?
            <Dashboard apiName={apiName}/> :
            <LoginScreen setUserLoggedIn={setUserLoggedIn} version={apiVersion}/>}
        </>
    )
}