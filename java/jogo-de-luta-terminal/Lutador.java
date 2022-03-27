public abstract class Lutador{

    private String nome = "Não definido";
    private Integer level = 1;
    private Integer velEvolucao = 1;
    private Integer vida = 10;
    private Integer energia = 10;
    private Integer forca = 0;
    private Integer agilidade = 0;
    private Integer resistencia = 0;
    private Integer experiencia = 0;


    public void uparLevel(){

        Integer expNecessaria = this.getLevel() * 10;

        if(this.getExperiencia() >= expNecessaria){

            this.setLevel(this.getLevel() + 1);
            this.setExperiencia(this.getExperiencia() - expNecessaria);
            System.out.println(String.format("%s subiu para o level %d",this.getNome(),this.getLevel()));

            this.setVida(this.getVida() + (this.getVelEvolucao() * 5));
            this.setEnergia(this.getEnergia() + (this.getVelEvolucao() * 4));
            this.setForca(this.getForca() + (this.getVelEvolucao() * 3));
            this.setAgilidade(this.getAgilidade() + (this.getVelEvolucao() * 3));
            this.setResistencia(this.getResistencia() + (this.getVelEvolucao() * 3));

        }

    }

    public void lutar(Lutador lutador1, Lutador lutador2){

    }

    public void setExperiencia(Integer experiencia) {
        this.experiencia += experiencia;
        this.uparLevel();
    }

    public Integer getExperiencia() {
        return experiencia;
    }

    public void setVelEvolucao(Integer velEvolucao) {
        this.velEvolucao = velEvolucao;
    }

    public Integer getVelEvolucao() {
        return velEvolucao;
    }


    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getNome() {
        return nome;
    }

    public void setLevel(Integer level) {

        if(level >= 1){
            this.level = level;
        }
        
    }

    public Integer getLevel() {
        return level;
    }

    public void setVida(Integer vida) {
        this.vida = vida;
    }

    public Integer getVida() {
        return vida;
    }

    public void setEnergia(Integer energia) {
        this.energia = energia;
    }

    public Integer getEnergia() {
        return energia;
    }

    public void setForca(Integer forca) {
        this.forca = forca;
    }

    public Integer getForca() {
        return forca;
    }

    public void setAgilidade(Integer agilidade) {
        this.agilidade = agilidade;
    }

    public Integer getAgilidade() {
        return agilidade;
    }

    public void setResistencia(Integer resistencia) {
        this.resistencia = resistencia;
    }

    public Integer getResistencia() {
        return resistencia;
    }




}