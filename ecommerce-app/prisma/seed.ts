import { PrismaClient } from '@prisma/client'
const prisma = new PrismaClient()
async function main() {
  await prisma.product.createMany({
    data: [
      { name: "Tシャツ", description: "快適なコットンTシャツ", price: 2000, imageUrl: "/images/tshirt.jpg" },
      { name: "マグカップ", description: "おしゃれなマグカップ", price: 1200, imageUrl: "/images/mug.jpg" }
    ]
  })
}
main()
  .catch(e => { throw e })
  .finally(async () => { await prisma.() })
