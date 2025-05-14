import { readFileSync, writeFileSync, existsSync } from 'fs';

// 获取环境变量
const cacheFile = process.env.CACHE_FILE || './timestamp.txt';

// 获取当前时间戳（单位：秒）
const currentTimestamp = Math.floor(Date.now() / 1000);

// 读取缓存的时间戳
let cachedTimestamp = 0;
if (existsSync(cacheFile)) {
  try {
    cachedTimestamp = parseInt(readFileSync(cacheFile, 'utf8').trim(), 10);
    console.log(`Cached Timestamp: ${cachedTimestamp}`);
  } catch (err) {
    console.error('Error reading cache file:', err);
  }
} else {
  console.log('No cache file found. Initializing timestamp to 0.');
}

// 比较时间戳
const timeDifference = currentTimestamp - cachedTimestamp;
console.log(`Current Timestamp: ${currentTimestamp}`);
console.log(`Time Difference: ${timeDifference} seconds`);

let updateCache = false;
if (timeDifference > 3600) {
  console.log('More than 1 hour has passed since the last run. Updating cache...');
  writeFileSync(cacheFile, currentTimestamp.toString());
  updateCache = true;
} else {
  console.log('Less than 1 hour has passed since the last run. Cache will not be updated.');
}

// 输出到 GitHub Actions 的上下文
console.log(`::set-output name=update_cache::${updateCache}`);