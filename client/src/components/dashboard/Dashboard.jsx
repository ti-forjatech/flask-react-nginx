import React from "react";

export default function Dashboard(props) {
    const msg = `Usuario logado com sucesso. Seja bemvindo a ${props.apiName}!`
    return (
        <>
            <section>
                <h2>Dashboard</h2>
                <p>{msg}</p>
            </section>
        </>
    )
}