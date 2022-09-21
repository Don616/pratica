import React from "react";
import Barriga from '../../assets/barriga.png';

export default function Header(){
    return(
        <header>
            <img src={Barriga}/>
            <h1>Logo</h1>
        </header>
    )
}