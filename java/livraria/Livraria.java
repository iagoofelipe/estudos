package livraria;

public class Livraria {
    public static void main(String args[]){
        Autor autor = new Autor();
        autor.nome = "José Almeida";
        autor.cpf = "123.456.789-10";
        autor.email = "jose@gmail.com";
        
        Autor outroAutor = new Autor();
        outroAutor.nome = "Maria Almeida";
        outroAutor.cpf = "123.886.789-98";
        outroAutor.email = "maria@gmail.com";
        


        Livro livro1 = new Livro();
        livro1.autor = new Autor();
        livro1.nome = "Java Em Dia";
        livro1.valor = 10.80;
        livro1.autor = autor;

        Livro livro2 = new Livro();
        livro2.autor = new Autor();
        livro2.nome = "Java Mais";
        // livro2.autor = autor;
        livro2.valor = 11.00;
        // livro2.autor.nome = "Guilherme Silva";


        // livro1.aplicaDescontoDe(0.1);
        livro2.aplicaDescontoDe(0.1);
        livro1.Mostrar();
        livro2.Mostrar();


        if(livro2.temAutor()) {
            System.out.println("Possui autor");
        }
        else {
            System.out.println("Não possui autor");
        }
    }
}


class Autor {
    String nome;
    String cpf;
    String email;

    void Mostrar() {
        System.out.println("Autor: " + nome);
        System.out.println("CPF do autor: " + cpf);
    }
}

class Livro {
    String nome;
    String codigo;
    double valor;
    Autor autor;


    void Mostrar(){
        System.out.println("Detalhes do Livro");
        System.out.println("Título do Livro:  " + nome);
        System.out.println("Valor:  " + valor);
        
        if(this.temAutor()) {
            autor.Mostrar();
        }

        System.out.println("--");
    };


    public void aplicaDescontoDe(double desconto){
        this.valor -= this.valor * desconto;
    }

    boolean temAutor() {
        return this.autor.nome != null;
    }
}

