const { MongoClient } = require("mongodb");

// Replace the uri string with your MongoDB deployment's connection string.
const uri = "mongodb://localhost:27017";

const client = new MongoClient(uri);

async function run() {
  try {
    await client.connect();

    const database = client.db('bancodb');

    // =============================================
    // Insert customers 
    // =============================================
    const customersCollection = database.collection('customers');
    await customersCollection.deleteMany();

    const customersDocs = [
      { nombre: 'Jaime Limón', clabe: 15, tipo: 'cliente', productos: ['cheque'] },
      { nombre: 'Rafael García', clabe: 25, tipo: 'cliente', productos: ['cheque'] },
      { nombre: 'Rodolfo López', clabe: 35, tipo: 'empresa', productos: ['tarjeta debito'] },
      { nombre: 'Juan Rivas', clabe: 45, tipo: 'empresa', productos: ['inversion'] },
    ];
    await customersCollection.insertMany(customersDocs);

    // =============================================
    // Insert transactions 
    // =============================================
    const transactionsCollection = database.collection('transactions');
    await transactionsCollection.deleteMany();

    const rafaDoc = await customersCollection.findOne({ nombre: 'Rafael García', productos: 'cheque' });
    await transactionsCollection.insertMany([
      {
        customerId: rafaDoc._id,
        monto: 1000,
        fecha: new Date(),
        producto: rafaDoc.productos[0],
        nombre: rafaDoc.nombre,
        medio: 'celular'
      },
      {
        customerId: rafaDoc._id,
        monto: -100,
        fecha: new Date(),
        producto: rafaDoc.productos[0],
        nombre: rafaDoc.nombre,
        medio: 'sucursal'
      }
    ]);

    const jaimeDoc = await customersCollection.findOne({ nombre: 'Jaime Limón', productos: 'cheque' });
    await transactionsCollection.insertOne({
      customerId: jaimeDoc._id,
      monto: 999,
      fecha: new Date('2020-09-01'),
      producto: rafaDoc.productos[0],
      nombre: jaimeDoc.nombre,
      medio: 'sucursal'
    });

    const juanDoc = await customersCollection.findOne({ nombre: 'Juan Rivas', productos: 'inversion' });
    await transactionsCollection.insertMany([
      {
        customerId: juanDoc._id,
        monto: 10000,
        fecha: new Date("2020-09-04"),
        producto: juanDoc.productos[0],
        nombre: juanDoc.nombre,
        medio: 'sucursal'
      },
      {
        customerId: juanDoc._id,
        monto: 5000,
        fecha: new Date("2020-09-04"),
        producto: juanDoc.productos[0],
        nombre: juanDoc.nombre,
        medio: 'celular'
      }
    ]);

    // =============================================
    // Queries
    // =============================================
    // 
    // #a. El tipo de productos que maneja un cliente dado.
    // 
    const customerName = 'Jaime Limón'
    const customerByName = await customersCollection.findOne({ nombre: customerName });
    console.log(customerByName);
    // 
    // #b. La cantidad total de clientes que manejan inversiones.
    // 
    const countWithProduct = await customersCollection.countDocuments({ productos: 'inversion' });
    console.log(countWithProduct);
    // 
    // #c. El nombre de los clientes que hicieron depósitos o retiros la semana pasada
    // 
    const names = await transactionsCollection.distinct('nombre', {
      fecha: {
        $gte: new Date("2020-08-31"),
        $lt: new Date("2020-09-05")
      }
    });
    console.log(names);
    // 
    // #d. El nombre de los clientes, y el día, que hicieron retiros superiores a un monto dado..
    //
    const amount = 1000;
    const nomDayGivenAmount = await transactionsCollection.find({
      monto: {
        $gte: amount
      }
    }, { projection: { nombre: 1, fecha: 1, _id: 0 } }).toArray();
    console.log(nomDayGivenAmount);
    // 
    // #e. Los montos de los depósitos y retiros que se hicieron para un producto dado en un rango de fechas
    //
    const montos = await transactionsCollection.find({
      producto: 'inversion',
      fecha: {
        $gte: new Date("2020-08-31"),
        $lt: new Date("2020-09-05")
      }
    }, { projection: { monto: 1, _id: 0 } }).toArray();
    console.log(montos);
    // 
    // #f. El nombre de los productos, y del medio, que tuvieron depósitos superiores a un monto
    //
    const productosMedios = await transactionsCollection.find({
      monto: {
        $gte: 1000
      }
    }, { projection: { producto: 1, medio: 1, _id: 0 } }).toArray();
    console.log(productosMedios);


  } finally {
    // Ensures that the client will close when you finish/error
    await client.close();
  }
}

run().catch(console.dir);