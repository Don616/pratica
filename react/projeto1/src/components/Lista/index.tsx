import React, { useState } from "react";
import { ITarefa } from "../../types/tarefa";
import Item from "./Item";
import style from './Lista.module.scss';


function Lista({tarefas}:{tarefas: ITarefa[]}){
    
    return(
        <aside className={style.listaTarefas}>
            <h2 onClick={() =>{
                setTarefas([ ...tarefas, {tarefa: "Estudar estado", tempo: "05:00:00"}])
            }}>Estudos do dia</h2>
            <ul>
                {tarefas.map((item,index)=>(
                    <Item
                        key={index}
                        tarefa={item.tarefa}
                        tempo={item.tempo}
                    />    
                ))}
            </ul>
        </aside>
    )
}

export default Lista;

function setTarefas(arg0: ITarefa[]) {
    throw new Error("Function not implemented.");
}
