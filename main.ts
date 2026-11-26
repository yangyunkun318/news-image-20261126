// THE WORLD — Thursday 26 November 2026 (news-image-20261126 entry).
//
// One newspaper front page summing up the world's news of 26 November
// 2026 in a single 1024x1024 image. The page was drawn ahead of time by
// render.py (Pillow: flat vector scenes plus real text, deterministic) and
// ships in this repository as entry.png. This program's only job is to
// carry that file to the output directory, after checking the PNG
// signature, the 1024x1024 dimensions and the 1 MiB size limit.
//
// Try it outside the grader's container with:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const PNG_MAGIC = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);
const MAX_SIDE = 1024;
const MAX_BYTES = 1024 * 1024;

const here = dirname(fileURLToPath(import.meta.url));
const png = readFileSync(join(here, 'entry.png'));

if (!png.subarray(0, 8).equals(PNG_MAGIC)) {
  throw new Error('entry.png is not a PNG');
}
// The IHDR chunk stores width and height as big-endian uint32s at
// byte offsets 16 and 20.
const width = png.readUInt32BE(16);
const height = png.readUInt32BE(20);
if (width > MAX_SIDE || height > MAX_SIDE) {
  throw new Error(`image too big: ${width}x${height}`);
}
if (png.length > MAX_BYTES) {
  throw new Error(`image over 1 MiB: ${png.length} bytes`);
}

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outDir, { recursive: true });
writeFileSync(join(outDir, 'entry.png'), png);
console.log(`wrote entry.png (${width}x${height}, ${png.length} bytes)`);
