
const insere_arquivos = window.document.querySelector("input#pdf_file")
const botao = window.document.querySelector("input.botao")
let lista = document.querySelector("ul.listagem")

insere_arquivos.addEventListener("change",inserindo)


function inserindo(){
    lista.innerHTML = ''
    const arquivos = window.document.querySelector("input#pdf_file").files
    const lista_arquivos = window.document.querySelector("section.lista_arquivos")


    for(let c = 0 ; c < arquivos.length ; c++){
        let li = document.createElement("li")
        li.innerText = arquivos[c].name
        lista.appendChild(li)
    }

    lista_arquivos.appendChild(lista)
}


const insere_arquivos_merge = window.document.querySelector("input#pdf_merge")
const lista_merge = window.document.querySelector("ul.listagem")
insere_arquivos_merge.addEventListener("change",inserindo_merge)

function inserindo_merge(){
    lista_merge.innerHTML = ''
    const arquivos_merge = window.document.querySelector("input#pdf_merge").files


    for(let c = 0 ; c < arquivos_merge.length ; c++){
        let li = document.createElement("li")
        li.innerText = arquivos_merge[c].name
        lista_merge.appendChild(li)
}
}

botao.addEventListener("click",()=>{
    lista_merge.innerHTML = ''
    window.document.querySelector('input#pdf_file').value = ''
})



window.document.querySelector("img.converte_excel").addEventListener("click",()=>{
    window.document.querySelector("section.lista_arquivos").style.display = "block"
    window.document.querySelector("section.arquivos").style.display = "Flex"
    window.document.querySelector("section.merge").style.display = "None"
    window.document.querySelector('input#pdf_file').value = ''
    window.document.querySelector('input#pdf_merge').value = ''

    window.document.querySelector("ul.listagem").innerHTML = ''

})

window.document.querySelector("img.combina_pdf").addEventListener("click",()=>{
    window.document.querySelector("section.merge").style.display = "flex"
    window.document.querySelector("section.arquivos").style.display = "None"
    window.document.querySelector('input#pdf_file').value = ''
    window.document.querySelector('input#pdf_merge').value = ''

    window.document.querySelector("ul.listagem").innerHTML = ''
})