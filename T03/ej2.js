const { MongoClient } = require("mongodb");

// Replace the uri string with your MongoDB deployment's connection string.
const uri = "mongodb://localhost:27017";

const client = new MongoClient(uri);

async function run() {
  try {
    await client.connect();

    const database = client.db('supercito');

    // =============================================
    // Insert cliente 
    // =============================================
    const customersCollection = database.collection('cliente');
    await customersCollection.createIndex({ email: 1 }, { unique: true });
    await customersCollection.deleteMany();

    const customersDocs = [
      { nombre: 'Jaime Limón', email: 'jalisa@gmail.com' },
      { nombre: 'Rafael García', email: 'rafa@gmail.com' },
      { nombre: 'Ana Tovar', email: 'atovar@gmail.com' },
    ];
    await customersCollection.insertMany(customersDocs);

    // =============================================
    // Insert tiendas 
    // =============================================
    const storeCollection = database.collection('sucursal');
    await storeCollection.createIndex({ nombre: 1 }, { unique: true });
    await storeCollection.deleteMany();

    const storesDocs = [
      { nombre: 'Insurgentes Sur', ubicacion: 'Insurgentes Sur no. 00001' },
      { nombre: 'Tlalpan Centro', ubicacion: 'Calzada de Tlalpan no. 00001' },
      { nombre: 'Insurgentes Centro', ubicacion: 'Insurgentes no. 9999' },
    ];
    await storeCollection.insertMany(storesDocs);

    // =============================================
    // Insert compras 
    // =============================================
    const salesCollection = database.collection('compras');
    await salesCollection.deleteMany();
    let compras = [];

    let customer = await customersCollection.findOne({ nombre: 'Jaime Limón' });
    let sucursal = await storeCollection.findOne({ nombre: 'Insurgentes Sur' });
    compras.push(
      { 
        sucursalId: sucursal._id,
        clienteId: customer._id,
        fecha: new Date('2020-09-01'),
        productos: [
          {
            nombre: 'arroz',
            cantidad: 3,
            precioUnidad: 25.50
          },
          {
            nombre: 'huevo',
            cantidad: 2,
            precioUnidad: 39.90
          },
          {
            nombre: 'tortilla 12',
            cantidad: 1,
            precioUnidad: 12.49
          }
        ]
      }
    );
    customer = await customersCollection.findOne({ nombre: 'Rafael García' });
    compras.push(
      { 
        sucursalId: sucursal._id,
        clienteId: customer._id,
        fecha: new Date('2020-09-02'),
        productos: [
          {
            nombre: 'huevo',
            cantidad: 2,
            precioUnidad: 39.90
          },
        ]
      }
    );
    sucursal = await storeCollection.findOne({ nombre: 'Tlalpan Centro' });
    compras.push(
      { 
        sucursalId: sucursal._id,
        clienteId: customer._id,
        fecha: new Date('2020-09-05'),
        productos: [
          {
            nombre: 'aceite',
            cantidad: 1,
            precioUnidad: 50
          },
          {
            nombre: 'tortilla 12',
            cantidad: 2,
            precioUnidad: 12.49
          }
        ]
      }
    );
    await salesCollection.insertMany(compras);

    // =============================================
    // Queries
    // =============================================
    // 
    // #a. Cantidad total de clientes que acudieron a una sucursal en una fecha específica
    // 
    const clientesFecha = await salesCollection.distinct('clienteId', {
      sucursalId: sucursal._id,
      fecha: new Date('2020-09-05')
    });
    console.log(clientesFecha.length);
    // 
    // #b. Cantidad total de clientes que acudieron a todas las sucursales en un día
    // 
    const totClienteesSuc = await salesCollection.distinct('clienteId', {
      fecha: new Date('2020-09-05')
    });
    // 
    // c. Los productos que adquirió un cliente dado en una fecha dada. 
    // 
    const productosCliente = await salesCollection.find({
      clienteId: customer._id,
      fecha: new Date('2020-09-05')
    }, { projection: { productos: 1, _id: 0 } }).toArray();
    console.log(productosCliente);
    // 
    // d. El nombre de los clientes que acudieron a comprar el mes pasado. 
    // 
    const distinctIds = await salesCollection.distinct('clienteId', {
      fecha: {
        $gte: new Date("2020-08-31"),
        $lt: new Date("2020-09-31")
      }
    });
    const clientesMes = await customersCollection.find({
      _id: {
        $in: distinctIds
      }
    }).toArray();
    console.log(clientesMes);
    // 
    // e. La cantidad total de productos (tipos, no unidades) que se vendieron en un día concreto. 
    //

  } finally {
    // Ensures that the client will close when you finish/error
    await client.close();
  }
}

run().catch(console.dir);