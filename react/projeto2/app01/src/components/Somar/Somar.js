import React from "react";
import Mensagem from "../Mensagem/Mensagem";

export default function Somar(){

    const soma = (n1,n2) =>{
        return n1+n2;
    }

    return(
        <Mensagem soma={soma}/>
    )

}