# 373. Find K Pairs with Smallest Sums
https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

## ルール
- **Step 1**: まず自力で15分。詰まったら参考を1つだけ開いて読む → 閉じて要約 → 自分で実装 → AC
- **Step 2**: 自分なりに整形 → 他人のコードを読んで再整形 → PR でレビュー依頼
- **Step 3**: レビュー反映 → 10分以内にエラーなく書く

## Step 1 (2026-06-04, ?? min, ??)

### 1-A: 自力で考えたこと
- データ構造案: min heapのvalueを配列？tuple？にする
- アルゴリズム案: またbucket sortとmin heapを組み合わせて解けそう
- なんでincreading orderじゃなくて、わざわざnon-decreasing orderと強調したのか気になった。
> increasing order = 必ず前より大きい（重複なし）: 1, 2, 3, 4
> non-decreasing order = 前以上（重複あり）: 1, 1, 2, 3
 らしい。へぇ claude on webは端的かつ返信が短いのがいい。ChatGPTは1行の質問に対して1000文字くらい返ってくるからtoo much 


### 1-B: 詰まった点
- tupleと配列の違いがよくわからなかった

### 1-C: 自分が理解した解法
- heapに入れて、heapから取り出す

### 1-D: 実装
```python
import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
      heap = []
      for j in range(len(nums2)):
        heapq.heappush(heap, (nums1[0] + nums2[j], 0, j))

      result = []
      for _ in range(k):
        total, i, j = heapq.heappop(heap)
        result.append([nums1[i], nums2[j]])

        if i + 1 < len(nums1):
          heapq.heappush(heap, (nums1[i+1] + nums2[j], i + 1, j))
        
      return result
```

## Step2
- iとかjとか、わかりにくいのだろうか。単なるインデックスとして利用している分には、監修から逸脱していないのだろうか


```python
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
      heap = []
      for j in range(len(nums2)):
        heapq.heappush(heap, (nums1[0] + nums2[j], 0, j)

      result = []
      for _ in range(k):
        total, i, j = heapq.heappop(heap)
        result.append([nums1[i], nums2[j]])

        if i + 1 < len(nums1):
            heapq.heappush(heap, (nums1[i+1] + nums2[j], i + 1, j))
      return result        

```

- iteratorを使ってこんな書き方もあるみたい。
```python
import heapq

def k_smallest_pairs(nums1, nums2, k):
    def generate():
        heap = [(nums1[0] + nums2[j], 0, j) for j in range(len(nums2))]
        heapq.heapify(heap)
        while heap:
            total, i, j = heapq.heappop(heap)
            yield [nums1[i], nums2[j]]
            if i + 1 < len(nums1):
                heapq.heappush(heap, (nums1[i+1] + nums2[j], i+1, j))
    
    return list(itertools.islice(generate(), k))
```


## 参考
- https://github.com/mamo3gr/arai60/pull/10
- https://github.com/olsen-blue/Arai60/pull/10
- https://github.com/Yoshiki-Iwasa/Arai60/pull/9
- https://github.com/h-masder/Arai60/pull/11
- https://github.com/Shunii85/arai60/pull/10
- https://discord.com/channels/1084280443945353267/1200089668901937312/1207200647594639391
> 一般に、コードを読むのは、ワーキングメモリーを使う行為です。
>変数の意味であったり、何が入っていて、どういう処理がなされて、その時点で、どういう値が入る可能性があって、この関数は、例外を投げる可能性があるんだっけないんだっけ。
>そういうことを考えながら頭の中で走らせています。だから、ワーキングメモリーをさっさと開放してあげることが大事です。



```python
import heapq

heap = []
heapq.heappush(heap, (値, i, j))  # 追加
heapq.heappop(heap)               # 最小を取り出す
```