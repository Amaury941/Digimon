const OrientDBClient = require('orientjs').OrientDBClient;

async function findPath(startName, endName) {
  console.log(`Procurando caminho de ${startName} para ${endName}...`);
  const client = await OrientDBClient.connect({
    host: 'localhost',
    port: 2424,
    username: 'root',
    password: 'rootpwd'
  });

  const db = await client.session({
    name: 'DigimonCyberSleuth',
    type: 'graph',
    username: 'root',
    password: 'rootpwd'
  });

  const digimons = await db.query('SELECT FROM Digimon').all();
  const start = digimons.find(d => d.Name === startName);
  const end = digimons.find(d => d.Name === endName);

  async function bfs(start, end) {
    const queue = [start];
    const visited = new Set();
    const predecessor = {};

    while (queue.length > 0) {
      const current = queue.shift();

      if (current.Name === end.Name) {
        const path = [];
        let node = end;
        while (node.Name !== start.Name) {
          path.push(node.Name);
          node = predecessor[node['@rid'].toString()];
        }
        path.push(start.Name);
        return path.reverse();
      }

      const neighbors = await db.query(`SELECT expand(out('Digivolves_to')) FROM ${current['@rid']}`).all();

      for (const neighbor of neighbors) {
        if (!visited.has(neighbor)) {
          visited.add(neighbor);
          predecessor[neighbor['@rid'].toString()] = current;
          queue.push(neighbor);
        }
      }
    }

    return null;
  }

  const path = await bfs(start, end);
  if (path === null) {
    console.log(`Caminho de ${startName} para ${endName} não encontrado.`);
  } else {
    console.log(`Caminho de ${startName} para ${endName}:`);
    console.log(path);
  }
  client.close()
}

function main() {
  findPath('Botamon', 'HerculesKabuterimon');
}

main();
