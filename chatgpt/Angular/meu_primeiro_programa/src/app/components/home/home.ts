export class AppComponent {

    nome: string = "";
    mensagem: string = "";

    mostrarMensagem() {
        this.mensagem = `Olá, ${this.nome}!`;
    }

}
