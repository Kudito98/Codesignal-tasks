<p>Given an array of equal-length strings, you'd like to know if it's possible to rearrange the order of the elements in such a way that each consecutive pair of strings differ by exactly one character. Return <code>true</code> if it's possible, and <code>false</code> if not.</p>
<p><strong>Note: You're only rearranging the order of the strings, not the order of the letters within the strings!</strong></p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For <code>inputArray = ["aba", "bbb", "bab"]</code>, the output should be<br />
<code>solution(inputArray) = false</code>.</p>
<p>There are 6 possible arrangements for these strings:</p>
<ul>
<li><code>["aba", "bbb", "bab"]</code></li>
<li><code>["aba", "bab", "bbb"]</code></li>
<li><code>["bbb", "aba", "bab"]</code></li>
<li><code>["bbb", "bab", "aba"]</code></li>
<li><code>["bab", "bbb", "aba"]</code></li>
<li><code>["bab", "aba", "bbb"]</code></li>
</ul>
<p>None of these satisfy the condition of consecutive strings differing by 1 character, so the answer is <code>false</code>.</p>
</li>
<li>
<p>For <code>inputArray = ["ab", "bb", "aa"]</code>, the output should be<br />
<code>solution(inputArray) = true</code>.</p>
<p>It's possible to arrange these strings in a way that each consecutive pair of strings differ by 1 character (eg: <code>"aa", "ab", "bb"</code> or <code>"bb", "ab", "aa"</code>), so return <code>true</code>.</p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.string inputArray</strong></p>
<p>A non-empty array of strings of lowercase letters.</p>
<p><em>Guaranteed constraints:</em><br />
<code>2 ≤ inputArray.length ≤ 10</code>,<br />
<code>1 ≤ inputArray[i].length ≤ 15</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p>Return <code>true</code> if the strings can be reordered in such a way that each neighbouring pair of strings differ by exactly one character (<code>false</code> otherwise).</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
