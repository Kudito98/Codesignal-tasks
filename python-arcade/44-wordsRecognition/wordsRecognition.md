<p>You are working on an AI that can recognize words. To begin with, you'd like to try the following approach: for the given pair of words the AI should find two strings of sorted letters that uniquely identify these words.</p>
<p>Given words <code>word1</code> and <code>word2</code>, return an array of two strings sorted <a href="keyword://lexicographical-order-for-strings" target="_blank">lexicographically</a>, where the first string contains characters present only in <code>word1</code>, and the second string contains characters present only in <code>word2</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>word1 = "program"</code> and <code>word2 = "develop"</code>,<br />
the output should be<br />
<code>solution(word1, word2) = ["agmr", "delv"]</code>.</p>
<p>Letters <code>'o'</code> and <code>'p'</code> are present in both words, and other letters identify them uniquely.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string word1</strong></p>
<p>The first word consisting of lowercase English letters.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ word1.length ≤ 20</code>.</p>
</li>
<li>
<p><strong>[input] string word2</strong></p>
<p>The second word consisting of lowercase English letters.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ word2.length ≤ 20</code>.</p>
</li>
<li>
<p><strong>[output] array.string</strong></p>
<p>Array of two strings sorted <em>lexicographically</em>, where the first string uniquely identifies the first word, and the second string uniquely identifies the second word.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
