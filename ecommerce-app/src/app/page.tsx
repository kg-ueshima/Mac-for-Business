import { PrismaClient, Product } from '@prisma/client';

const prisma = new PrismaClient();

async function getProducts(): Promise<Product[]> {
  return await prisma.product.findMany();
}

export default async function Home() {
  const products = await getProducts();
  return (
    <main style={{ padding: 24 }}>
      <h1>サンプル商品一覧</h1>
      <ul style={{ listStyle: 'none', padding: 0 }}>
        {products.map((product) => (
          <li key={product.id} style={{ marginBottom: 24, border: '1px solid #ccc', borderRadius: 8, padding: 16 }}>
            <h2>{product.name}</h2>
            <p>{product.description}</p>
            <p>価格: {product.price}円</p>
            {product.imageUrl && (
              <img src={product.imageUrl} alt={product.name} style={{ maxWidth: 200 }} />
            )}
          </li>
        ))}
      </ul>
    </main>
  );
}
