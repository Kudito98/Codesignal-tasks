<p>An <em>alphanumeric</em> ordering of strings is defined as follows: each string is considered as a sequence of tokens, where each token is a letter or a number (as opposed to an isolated digit, as is the case in lexicographic ordering). For example, the tokens of the string <code>"ab01c004"</code> are <code>[a, b, 01, c, 004]</code>. In order to compare two strings, we'll first break them down into tokens and then compare the corresponding pairs of tokens with each other (i.e. compare the first token of the first string with the first token of the second string, etc).</p>
<p>Here is how tokens are compared:</p>
<ul>
<li>If a letter is compared with another letter, the usual alphabetical order applies.</li>
<li>A number is always considered <em>less</em> than a letter.</li>
<li>When two numbers are compared, their values are compared. Leading zeros, if any, are ignored.</li>
</ul>
<p>If at some point one string has no more tokens left while the other one still does, the one with fewer tokens is considered <em>smaller</em>.</p>
<p>If the two strings <code>s1</code> and <code>s2</code> appear to be equal, consider the smallest index <code>i</code> such that <code>tokens(s1)[i]</code> and <code>tokens(s2)[i]</code> (where <code>tokens(s)[i]</code> is the <code>i<sup>th</sup></code> token of string <code>s</code>) differ only by the number of leading zeros. If no such <code>i</code> exists, the strings are indeed equal. Otherwise, the string whose <code>i<sup>th</sup></code> token has more leading zeros is considered <em>smaller</em>.</p>
<p>Here are some examples of comparing strings using alphanumeric ordering.</p>
<pre><code>"a" &lt; "a1" &lt; "ab"
"ab42" &lt; "ab000144" &lt; "ab00144" &lt; "ab144" &lt; "ab000144x"
"x11y012" &lt; "x011y13"
</code></pre>
<p>Your task is to return <code>true</code> if <code>s1</code> is strictly less than <code>s2</code>, and <code>false</code> otherwise.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For <code>s1 = "a"</code> and <code>s2 = "a1"</code>, the output should be <code>solution(s1, s2) = true</code>;</p>
<p>These strings have equal first tokens, but since <code>s1</code> has fewer tokens than <code>s2</code>, it's considered smaller.</p>
</li>
<li>
<p>For <code>s1 = "ab"</code> and <code>s2 = "a1"</code>, the output should be <code>solution(s1, s2) = false</code>;</p>
<p>These strings also have equal first tokens, but since numbers are considered less than letters, <code>s1</code> is larger.</p>
</li>
<li>
<p>For <code>s1 = "b"</code> and <code>s2 = "a1"</code>, the output should be <code>solution(s1, s2) = false</code>.</p>
<p>Since <code>b</code> is greater than <code>a</code>, <code>s1</code> is larger.</p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string s1</strong></p>
<p>A string consisting of English letters and digits.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ s1.length ≤ 20</code>.</p>
</li>
<li>
<p><strong>[input] string s2</strong></p>
<p>A string consisting of English letters and digits.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ s2.length ≤ 20</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p><code>true</code> if <code>s1</code> is alphanumerically strictly less than <code>s2</code>, <code>false</code> otherwise.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
