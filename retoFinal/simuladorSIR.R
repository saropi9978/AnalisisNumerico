

#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#
library(shiny)

# Define UI for application that draws a histogram
ui <- fluidPage(
  
  # Application title
  titlePanel("Prueba modelo SIR"),
  
  sidebarLayout(
    sidebarPanel(
      helpText("Cambia el valor de los parametros del modelo"),
      selectInput("tipoModelo",
                  label = "Seleccione el modelo con el que quiere trabajar",
                  choices = list("adams",
                                 "rk4","euler"),
                  selected = "adams"),
      sliderInput("L",
                  "Valor del area:",
                  min = 6,
                  max = 20,
                  value = 10),
      sliderInput("r",
                  "Valor del radio:",
                  min = 0.5,
                  max = 2,
                  value = 2),
      sliderInput("beta",
                  "Valor beta (tasa de infeccion):",
                  min = 0.0001,
                  max = 0.0006,
                  value = 0.0003),
      sliderInput("gamma",
                  "Valor gamma (tasa recuperacion de nodos infectados):",
                  min = 0.001,
                  max = 0.005,
                  value = 0.0025),
      sliderInput("alpha",
                  "Valor alpha (tasa de nodos a suceptible):",
                  min = 0.041,
                  max = 0.300,
                  value = 0.100),
      sliderInput("sigma",
                  "Valor sigma (tasa de vacunación):",
                  min =  0.001,
                  max =  0.003,
                  value =  0.0014),
      sliderInput("S",
                  "Valor de total de suceptibles: ",
                  min = 0,
                  max = 1000,
                  value = 990),
      sliderInput("I",
                  "Valor de total de infectados: ",
                  min = 1,
                  max = 9,
                  value = 5),
      sliderInput("R",
                  "Valor de total de recuperados: ",
                  min = 0,
                  max = 5,
                  value = 0),
      sliderInput("V",
                  "Valor de vacunados: ",
                  min = 0,
                  max = 5,
                  value = 0),
      sliderInput("E",
                  "Valor de Expuestos : ",
                  min = 1,
                  max = 9,
                  value = 5),
      sliderInput("Tiempo",
                  "Dias",
                  min = 100,
                  max = 1000,
                  value = 500)
    ),
    
    # Show a plot of the generated distribution
    mainPanel(
      plotOutput("distPlot"),
      tableOutput("table1")
    )
  )
)

# Define server logic required to draw a histogram
server <- function(input, output) {
  
  output$distPlot <- renderPlot({
    #Se limpian los elementos creados con anterioridad
    #rm(list=ls())
    #Se limpia la consola para una mejor visualizacion
    library(deSolve)
    
    #Modelo basado en el escrito "An Epidemic model of Malware"
    
    SIR <- function(t, x, parametros){
      with(as.list(c(parametros, x)),{
        N <- sum(v_iniciales)
        dS <- (miu*N) - (phi*S*I) - (miu*S) -(siggma*S) + (epsilon*V) + (delta*R)
        dE <- (phi*S*I) - (miu+alpha)*E
        dI <- (alpha*E) - (miu+gammaa)*I
        dR <- (gammaa*I) - (miu+delta)*R
        dV <- (siggma*S) - (miu+epsilon)*V
        
        return(list(c(dS, dI, dR, dV, dE)))
      })
    }
    
    parametros <- c(
      miu = 0.001,
      beta = input$beta,
      alpha =  input$alpha,
      gammaa=input$gamma,
      epsilon=0.001,
      siggma = input$sigma,
      delta= 0.001,
      phi=(input$beta*input$r*input$r*3.14)/(input$L*input$L))
    
    v_iniciales <- c(S=input$S, I=input$I, R=input$R, V=input$V, E=input$E)
    
    dt <- seq(100, input$Tiempo, 10)
    
    sol = ode(y=v_iniciales, times=dt, func=SIR,parms=parametros, method = input$tipoModelo)
    
    # result = EpiDynamics::SIR(pars = parametros, init = v_iniciales, time = dt)
    
    simulacion.si <- as.data.frame(sol)
    attach(simulacion.si)
    
    N <- sum(v_iniciales)
    plot(dt, S, type="l", col="blue", ylim=c(0,sum(v_iniciales)), xlab = "Tiempo (Dias)", ylab="Numero de individuos (en miles)")
    lines(dt, I, type="l", col="red")
    lines(dt, R, type="l", col="green")
    lines(dt, V, type = "l", col = "brown")
    lines(dt, E, type = "l", col = "orange")
    title("Modelo SIR")
    legend((input$Tiempo)/2, N + 0.25,
           legend=c("Suceptibles", "Infectados", "Recuperados", "Vacunados","Expuestos"),
           col=c("blue", "red", "green","brown", "orange"), lty=rep(1, 2))
    
    
    # #Calcular R0
    
    r0 <- (((input$beta)*(3.1416)*((input$r)*(input$r))*(sum(v_iniciales))*(0.001 + 0.001)*(input$alpha))/((input$L * input$L)*(0.001 + input$alpha)*(0.001 + input$gamma)*(0.001 + 0.001 + input$sigma)))
    
    output$table1 <- renderTable(data.frame(a = 1L, date = "7 Jan 17", b = 80L, c = 80L, d = -4L,
                                            e = 26L, f = 58L, g = 16L, h = 12L, i = 12L, R0= r0))
  
  })
}

# Run the application
shinyApp(ui = ui, server = server)


