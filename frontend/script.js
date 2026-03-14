async function loadStatus(){


const res = await fetch("http://127.0.0.1:5000/status")
const data = await res.json()


/* UPDATE CARDS */


document.getElementById("carbonValue").innerText =
data.carbon_intensity + " gCO₂/kWh"


document.getElementById("runningContainers").innerText =
data.running_containers.length


document.getElementById("stoppedContainers").innerText =
data.stopped_containers.length



/* SYSTEM MODE */


if(data.carbon_intensity > 400){


document.getElementById("systemMode").innerText = "High Carbon Mode"


document.getElementById("carbonAlert").classList.remove("hidden")


modeChart.data.datasets[0].data=[0,1]


}else{


document.getElementById("systemMode").innerText = "Low Carbon Mode"


document.getElementById("carbonAlert").classList.add("hidden")


modeChart.data.datasets[0].data=[1,0]


}


modeChart.update()


/* UPDATE GRAPH */


updateGraph(data.carbon_intensity)


/* UPDATE ACTIVITY FEED */


updateActivity(data)


}




/* GRAPH DATA */


let labels=[]
let carbonHistory=[]




/* CARBON LINE CHART */


const ctx=document.getElementById("carbonChart").getContext("2d")


const carbonChart=new Chart(ctx,{


type:"line",


data:{
labels:labels,


datasets:[{
data:carbonHistory,


borderColor:"#d946ef",
backgroundColor:"rgba(217,70,239,0.25)",


borderWidth:3,


pointRadius:4,
pointHoverRadius:7,


fill:true,


tension:0.45
}]


},


options:{


animation:{
duration:900,
easing:"easeOutQuart"
},


plugins:{
legend:{display:false}
},


interaction:{
intersect:false,
mode:"index"
},


scales:{
x:{grid:{color:"rgba(255,255,255,0.05)"}},
y:{grid:{color:"rgba(255,255,255,0.05)"}}
}


}


})




/* GRAPH UPDATE */


function updateGraph(value){


const time=new Date().toLocaleTimeString()


labels.push(time)
carbonHistory.push(value)


/* keep last 15 points */


if(labels.length>15){


labels.shift()
carbonHistory.shift()


}


carbonChart.update()


}




/* DONUT CHART */


const modeCtx=document.getElementById("modeChart").getContext("2d")


const modeChart=new Chart(modeCtx,{


type:"doughnut",


data:{
labels:["Low Carbon","High Carbon"],


datasets:[{
data:[1,0],


backgroundColor:[
"#4ade80",
"#ff5a7a"
]


}]


},


options:{
plugins:{
legend:{
labels:{color:"#ddd"}
}
}
}


})




/* ACTIVITY LOG */


function updateActivity(data){


const log=document.getElementById("activityLog")


const time=new Date().toLocaleTimeString()


const item=document.createElement("li")


item.innerText =
`${time} → Carbon ${data.carbon_intensity} | Running ${data.running_containers.length}`


log.prepend(item)


if(log.children.length>8){
log.removeChild(log.lastChild)
}


}




/* INITIAL LOAD */


loadStatus()




/* AUTO REFRESH */


setInterval(loadStatus,5000)




/* LIVE CLOCK */


setInterval(()=>{


document.getElementById("time").innerText =
new Date().toLocaleTimeString()


},1000)
0