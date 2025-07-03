#!/bin/bash

# Next.jsプロジェクト作成
echo "[1/8] Next.jsプロジェクト作成..."
npx create-next-app@latest ecommerce-app --typescript --eslint --tailwind --src-dir --app --import-alias "@/*" --no-interactive

cd ecommerce-app || exit 1

# 必要パッケージのインストール
echo "[2/8] 依存パッケージインストール..."
npm install @prisma/client prisma stripe react-stripe-js @stripe/stripe-js

# Prisma初期化
echo "[3/8] Prisma初期化..."
npx prisma init

# Prismaスキーマ作成
echo "[4/8] Prismaスキーマ作成..."
cat <<EOL > prisma/schema.prisma
generator client {
  provider = "prisma-client-js"
}
datasource db {
  provider = "sqlite"
  url      = "file:./dev.db"
}
model Product {
  id          Int      @id @default(autoincrement())
  name        String
  description String
  price       Int
  imageUrl    String
}
model User {
  id    Int    @id @default(autoincrement())
  email String @unique
  name  String
}
model Order {
  id        Int      @id @default(autoincrement())
  user      User     @relation(fields: [userId], references: [id])
  userId    Int
  products  Product[]
  total     Int
  createdAt DateTime @default(now())
}
EOL

# DBマイグレーション
echo "[5/8] DBマイグレーション..."
npx prisma migrate dev --name init --skip-seed

# サンプルデータ投入（seedスクリプト作成）
echo "[6/8] サンプルデータ投入..."
cat <<EOL > prisma/seed.ts
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
  .finally(async () => { await prisma.$disconnect() })
EOL

npm install ts-node @types/node --save-dev
npx ts-node prisma/seed.ts

# 必要なディレクトリ作成
echo "[7/8] ディレクトリ作成..."
mkdir -p src/app/products src/app/cart src/app/checkout src/components src/lib

# 完了メッセージ
echo "[8/8] セットアップ完了！"
echo "次のコマンドで開発サーバーを起動できます："
echo "cd ecommerce-app && npm run dev" 