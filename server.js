const spawner = require('child_process').spawn;

const pass_input = 'send';

console.log('Data sent to python script: ', pass_input);

const python_process = spawner('python', ['./python.py', JSON.stringify(pass_input)]);

python_process.stdout.on('data', (data) => {
    console.log('Data received from python script: ', data.toString());
});