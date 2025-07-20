/*
 Navicat Premium Data Transfer

 Source Server         : LOCAL_POSGRE
 Source Server Type    : PostgreSQL
 Source Server Version : 140008 (140008)
 Source Host           : localhost:5432
 Source Catalog        : fastapi_db
 Source Schema         : public

 Target Server Type    : PostgreSQL
 Target Server Version : 140008 (140008)
 File Encoding         : 65001

 Date: 21/07/2025 01:23:30
*/


-- ----------------------------
-- Sequence structure for products_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."products_id_seq";
CREATE SEQUENCE "public"."products_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;
ALTER SEQUENCE "public"."products_id_seq" OWNER TO "postgres";

-- ----------------------------
-- Table structure for products
-- ----------------------------
DROP TABLE IF EXISTS "public"."products";
CREATE TABLE "public"."products" (
  "id" int4 NOT NULL DEFAULT nextval('products_id_seq'::regclass),
  "name" varchar COLLATE "pg_catalog"."default",
  "price" float8,
  "quantity" int4
)
;
ALTER TABLE "public"."products" OWNER TO "postgres";

-- ----------------------------
-- Records of products
-- ----------------------------
BEGIN;
INSERT INTO "public"."products" ("id", "name", "price", "quantity") VALUES (1, 'Test', 1.23, 10);
COMMIT;

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."products_id_seq"
OWNED BY "public"."products"."id";
SELECT setval('"public"."products_id_seq"', 2, true);

-- ----------------------------
-- Indexes structure for table products
-- ----------------------------
CREATE INDEX "ix_products_id" ON "public"."products" USING btree (
  "id" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "ix_products_name" ON "public"."products" USING btree (
  "name" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "ix_products_price" ON "public"."products" USING btree (
  "price" "pg_catalog"."float8_ops" ASC NULLS LAST
);
CREATE INDEX "ix_products_quantity" ON "public"."products" USING btree (
  "quantity" "pg_catalog"."int4_ops" ASC NULLS LAST
);

-- ----------------------------
-- Primary Key structure for table products
-- ----------------------------
ALTER TABLE "public"."products" ADD CONSTRAINT "products_pkey" PRIMARY KEY ("id");
