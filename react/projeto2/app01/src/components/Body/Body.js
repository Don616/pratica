import React from "react";
import Mensagem from "../Mensagem/Mensagem";

export default function Body(props){

    const msg = "Mensagem padrão";
    const somar = (n1,n2) => {
        return n1+n2
    }

    return(
        <div>
            <Mensagem 
                somar={somar(1,5)}
            />
        </div>
    )
}