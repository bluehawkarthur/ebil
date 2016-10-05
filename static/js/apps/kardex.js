/**
*** OBJETOS Y VARIABLES NESESARIAS ***
**/
var datosKardex = [],
	datosSalidas = [],
	total = {"especie":0,"saldo":0};

/**
*** REFERENCIAS A DOM
**/
var	tablaKardex = document.getElementById("tablaKardex");
	cuerpoTablaKardex = tablaKardex.getElementsByTagName('tbody')[0],
	divCostoUnitario = document.getElementById("costoUnitario");

/**
*** FUNCIONES PRINCIPALES ***
**/
var registrar = {
	entrada: function(fecha,cantidadEntrada,valorUnitario,detalle,factura){
		var cantidadEntrada = parseInt(cantidadEntrada),
			valorUnitario = parseFloat(valorUnitario),

			detalle = detalle || "<span class=\"campoVacio\">(No especificado)</span>",
			factura = factura || "<span class=\"campoVacio\">(No especificado)</span>";
		var ins = {"tipo":"entrada","fecha":formato.fechaObj(fecha),"factura":factura,"detalle":detalle,"entrada":cantidadEntrada,"valor":valorUnitario};
		var ult = datosKardex.length - 1;
		var indice = 0;
		console.log(valorUnitario);
		if(ult === -1){
			datosKardex.push(ins);
		}else{
			for (var i = ult; i >= 0; i--) {
				if(datosKardex[i].fecha.getTime() < ins.fecha.getTime()){
					indice = i+1;
					datosKardex.splice(indice,0,ins);
					break;
				}
			};
		}
		//datosKardex.push(ins);
		total.especie += cantidadEntrada;
		total.saldo += cantidadEntrada*valorUnitario;
		insertarFilaEntrada(ins,indice);

	},
	salida: function(fecha,cantidadSalida,detalle,factura,typo){
		var cantidadSalida = parseInt(cantidadSalida),
			valorUnitario = parseFloat(valorUnitario),
			detalle = detalle || "<span class=\"campoVacio\">(No especificado)</span>",
			factura = factura || "<span class=\"campoVacio\">(No especificado)</span>";
		var ins = {"tipo":"salidaTitulo","fecha":formato.fechaObj(fecha),"factura":factura,"detalle":detalle,"salida":cantidadSalida};
		var ult = datosKardex.length - 1;
		var indice = 0;
		var filas = cuerpoTablaKardex.rows;
		var cantFilas = filas.length;
		for (var i = ult; i >= 0; i--) {
			if(datosKardex[i].fecha.getTime() < ins.fecha.getTime()){
				indice = i+1;
				break;
			}
		}
		if(parseInt(filas[indice-1].cells[8].innerHTML) >= cantidadSalida){
			insertarFilaTituloSalida(ins,indice);
			datosKardex.splice(indice,0,ins);
			//datosKardex.push(ins);
			total.especie -= cantidadSalida;
			var salidas = obtenerSalidasSegunMetodoSeleccionado(indice,cantidadSalida,formato.fechaObj(fecha),typo);
			
			for (var j = salidas.length - 1; j >= 0 ; j--) {
				insertarFilaSalida(salidas[j],indice+1);
				datosKardex.splice(indice+1,0,salidas[j]);
			};

			//total.saldo -= cantidadSalida*valorUnitario;
		
			
		}else{
			swal("Error!","Stock insuficiente para cumplir con esta salida","error");
		}

	}
}



var insertarFilaEntrada = function(obj,indice){
	console.log(obj.valor);
	fila = cuerpoTablaKardex.insertRow(indice);
	fila.dataset.tipo = "entrada";
	var celda = fila.insertCell(0);
	celda.innerHTML = formato.fechaStr(obj.fecha);



	celda = fila.insertCell(1);
	celda.innerHTML = obj.detalle;

	celda = fila.insertCell(2);
	celda.innerHTML = obj.entrada;
	fila.dataset.restante = obj.entrada;
	fila.dataset.total = obj.entrada;

	celda = fila.insertCell(3);
	celda.innerHTML = formato.decimales(obj.valor,2);

	celda = fila.insertCell(4);
	// celda.innerHTML = "<i class=\"fa fa-spinner\"></i>";
	celda.innerHTML = formato.decimales(obj.entrada * obj.valor,2);

	celda = fila.insertCell(5);
	//celda.innerHTML = formato.decimales(obj.valor,1);
	celda.innerHTML = "-";
	fila.dataset.vu = obj.valor;

	celda = fila.insertCell(6);
	celda.innerHTML = "-";

	celda = fila.insertCell(7);
	celda.innerHTML = "-";
	//celda.innerHTML = formato.decimales(obj.entrada * obj.valor,1);
	fila.dataset.debe = obj.entrada * obj.valor;

	celda = fila.insertCell(8);
	celda.innerHTML = "-";

	celda = fila.insertCell(9);
	celda.innerHTML = "<i class=\"fa fa-spinner\"></i>";

	
	calcularTotalesTabla();

//	cuerpoTablaKardex.appendChild(fila);
},insertarFilaTituloSalida = function(obj,indice){
	fila = cuerpoTablaKardex.insertRow(indice);
	fila.dataset.tipo = "tituloSalida";
	fila.classList.add("tituloSalida");
	var celda = fila.insertCell(0);
	celda.innerHTML = formato.fechaStr(obj.fecha);


	celda = fila.insertCell(1);
	celda.innerHTML = obj.detalle;

	celda = fila.insertCell(2);
	celda.innerHTML = "-";
	

	celda = fila.insertCell(3);
	//celda.innerHTML = obj.salida;
	celda.innerHTML = "-";
	fila.dataset.salida = obj.salida;

	celda = fila.insertCell(4);
	celda.innerHTML = "-";

	celda = fila.insertCell(5);
	//celda.innerHTML = "-";
	celda.innerHTML = obj.salida;

	celda = fila.insertCell(6);
	celda.innerHTML = "-";

	celda = fila.insertCell(7);
	celda.innerHTML = "-";

	celda = fila.insertCell(8);
	celda.innerHTML = "-";

	celda = fila.insertCell(9);
	celda.innerHTML = "-";

	

	calcularTotalesTabla();
}
,insertarFilaSalida = function(obj,indice){
	fila = cuerpoTablaKardex.insertRow(indice);
	fila.classList.add("filaSalida");
	fila.dataset.tipo = "salida";
	var celda = fila.insertCell(0);
	celda.innerHTML = formato.fechaStr(obj.fecha);

	

	celda = fila.insertCell(1);
	celda.innerHTML = "~";

	celda = fila.insertCell(2);
	celda.innerHTML = "-";

	celda = fila.insertCell(3);
	celda.innerHTML = "-";
	

	celda = fila.insertCell(4);
	//celda.innerHTML = "<i class=\"fa fa-spinner\"></i>";
	celda.innerHTML = "-";

	celda = fila.insertCell(5);
	//celda.innerHTML = "-";
	celda.innerHTML = obj.salida;
	fila.dataset.total = obj.salida;

	celda = fila.insertCell(6);
	celda.innerHTML = formato.decimales(obj.pu,2);

	celda = fila.insertCell(7);
	//celda.innerHTML = "-";
	celda.innerHTML = formato.decimales(obj.salida * obj.pu,2);
	fila.dataset.haber = obj.salida * obj.pu;

	celda = fila.insertCell(8);
	celda.innerHTML = "-";

	celda = fila.insertCell(9);
	celda.innerHTML = "<i class=\"fa fa-spinner\"></i>";



	calcularTotalesTabla();
},
obtenerSalidasSegunMetodoSeleccionado = function(pos,cant,fecha,typo){
	var tem = [];
	var filas = cuerpoTablaKardex.rows;
	var cantFilas = filas.length;
	switch(typo){
		case 'peps':
			var i;
			for (i = 0; i <= pos; i++) {
				if(filas[i].dataset.tipo === "entrada" && parseInt(filas[i].dataset.restante) > 0){
					if(parseInt(filas[i].dataset.restante) >= cant){
						filas[i].dataset.restante = parseInt(filas[i].dataset.restante) - cant;
						tem.push({"tipo":"salida","fecha":fecha,"salida":cant,"pu":parseFloat(filas[i].dataset.vu)});
						break;
					}else{
						cant = cant-parseInt(filas[i].dataset.restante);
						tem.push({"tipo":"salida","fecha":fecha,"salida":parseInt(filas[i].dataset.restante),"pu":parseFloat(filas[i].dataset.vu)});
						filas[i].dataset.restante = 0;
					}
				}
			};datosKardex

		break;
		case 'ueps':
			var i;
			for (i = pos-1; i >= 0; i--) {
				if(filas[i].dataset.tipo === "entrada" && parseInt(filas[i].dataset.restante) > 0){
					if(parseInt(filas[i].dataset.restante) >= cant){
						filas[i].dataset.restante = parseInt(filas[i].dataset.restante) - cant;
						tem.push({"tipo":"salida","fecha":fecha,"salida":cant,"pu":parseFloat(filas[i].dataset.vu)});
						break;
					}else{
						cant = cant-parseInt(filas[i].dataset.restante);
						tem.push({"tipo":"salida","fecha":fecha,"salida":parseInt(filas[i].dataset.restante),"pu":parseFloat(filas[i].dataset.vu)});
						filas[i].dataset.restante = 0;
					}
				}
			};
		break;
		case 'pp':
			var fila = filas[pos-1];
			var pu = parseFloat(fila.cells[9].innerHTML)/parseInt(fila.cells[8].innerHTML);
			tem.push({"tipo":"salida","fecha":fecha,"salida":cant,"pu":pu});
		break;
		default:

	}
	console.log(tem)
	return tem;
};

/***
** FUNCIONES CALCULAR ***
***/
var calcularTotalesTabla = function(){
	var filas = cuerpoTablaKardex.rows;
	var totalEspecie = 0;
	var saldoTotal = 0;
	var totalFilas = filas.length;
	var i;
	for(i = 0; i < totalFilas; i++){
		if(filas[i].dataset.tipo !== "tituloSalida"){
			if(filas[i].dataset.tipo === "entrada"){				
				totalEspecie += parseInt(filas[i].dataset.total);
				saldoTotal += parseFloat(filas[i].dataset.debe);	
			}else{
				totalEspecie -= parseInt(filas[i].dataset.total);
				saldoTotal -= parseFloat(filas[i].dataset.haber);
			}

			filas[i].cells[8].innerHTML = formato.decimales(totalEspecie,2);
			filas[i].cells[9].innerHTML = formato.decimales(saldoTotal,2);
		}
	}
};

/**
*** OTRAS FUNCIONES
**/

recalcularSalidas = function(){
	console.log(datosKardex)
	console.log("Recalculando salidas con la nueva metodologia");
	var i,total = datosKardex.length;
	cuerpoTablaKardex.innerHTML = "";

	for(i = 0; i<total;i++){
		if(datosKardex[i].tipo === "salida"){
			datosKardex.splice(i,1);
		}
	}
	console.log(datosKardex);
	//eliminart salidas de datosKardex
	//reponer
	//reimprimir
}


// $.ajax({
//       url: '/kardex_json/',
//       dataType: 'json',
//       type: 'GET',
//       success: function(datos) {
        
//         for (var d in datos){
//         	console.log(datos[d]);
//         	if (datos[d].motivo_movimiento == 'salida') {
//         		// fecha,cantidadSalida,detalle,factura
//         		registrar.salida(datos[d].fecha_transaccion,datos[d].cantidad,datos[d].detalle,'ddggg');
//         	}else{
//         		// fecha,cantidadEntrada,valorUnitario,detalle,factura
//         		var valorUnitario = 0;
//         		if (datos[d].motivo_movimiento == 'inicial') {
//         			valorUnitario = datos[d].precio_unitario;
//         		}else{
//         			valorUnitario = datos[d].precio_unitario / 100*87;
//         		};
//         		registrar.entrada(datos[d].fecha_transaccion,datos[d].cantidad,valorUnitario,datos[d].detalle,'fsf');
//         	};
//         }
//       }
// });

// CARGANDO POR DEFECTO POR METODO PROMEDIOS
agregarKardex('pp');

// FUNCION PARA AGREGAR SEGUN EL METODO ESCOGIDO EN KARDEX
function agregarKardex(typo) {
	$.ajax({
      url: '/kardex_json/'+$('#pk_item').val(),
      dataType: 'json',
      type: 'GET',
      success: function(datos) {
        
        for (var d in datos){
        	console.log(datos[d]);
        	if (datos[d].motivo_movimiento == 'salida') {
        		// fecha,cantidadSalida,detalle,factura
        		registrar.salida(datos[d].fecha_transaccion,datos[d].cantidad,datos[d].detalle,'ddggg', typo);
        	}else{
        		// fecha,cantidadEntrada,valorUnitario,detalle,factura
        		var valorUnitario = 0;
        		if (datos[d].motivo_movimiento == 'inicial') {
        			valorUnitario = datos[d].precio_unitario;
        		}else{
        			valorUnitario = datos[d].precio_unitario / 100*87;
        		};
        		registrar.entrada(datos[d].fecha_transaccion,datos[d].cantidad,valorUnitario,datos[d].detalle,'fsf');
        	};
        }
      }
	});
}

// FUNCION DE CAMBIO DE LOS RADIO BUTTONS
$('input[type=radio][name=kardex]').change(function() {
    if (this.value == 'pp') {
        
        $("#tablaKardex > tbody > tr").remove();
        datosKardex = new Array();
        tem = new Array();
        agregarKardex('pp');
    }
    else if (this.value == 'peps') {
   
  
        $("#tablaKardex > tbody > tr").remove();
        datosKardex = new Array();
        tem = new Array();
        agregarKardex('peps');
    }
});
// document.getElementById("tipoEspecie").onchange = function(a){
// 	if(a.target.selectedIndex === 1){
// 		divCostoUnitario.classList.remove('oculto');
// 	}else{
// 		divCostoUnitario.classList.add('oculto');
// 	}
// }