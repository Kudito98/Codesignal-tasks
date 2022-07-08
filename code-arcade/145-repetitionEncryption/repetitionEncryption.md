<p>Jane just got a <code>letter</code> from her friend and realized that something's wrong: some words in the <code>letter</code> are written twice in a row. The thing is, she and her friend devised an ingenious cypher, the key to which is the number of pairs of repeated words in the encoded text. The cases of the words don't matter.</p>
<p>Formally, a <em>word</em> is a <a href="keyword://substring" target="_blank">substring</a> of <code>letter</code> consisting of English letters, such that characters to the left of the leftmost letter and to the right of the rightmost letter are not letters.</p>
<p>For obvious reasons, Jane can't tell you how the encryption works, but she needs your help with calculating the number of pairs of consecutive equal words. Write a function that, given a <code>letter</code>, returns this number.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>letter = "Hi, hi Jane! I'm so. So glad to to finally be able to write - WRITE!! - to you!"</code>,<br />
the output should be<br />
<code>solution(letter) = 4</code>.</p>
<p>There are <code>4</code> pairs of consecutive identical words in the text. They are shown in different colors below:<br />
"<b><font color="red">Hi, hi</font></b> Jane! I'm <b><font color="blue">so. So</font></b> glad <b><font color="green">to to</font></b> finally be able to <b><font color="pink">write - WRITE</font></b>!! - to you!"</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string letter</strong></p>
<p>The letter Jane's friend wrote to her. It is guaranteed that there are no more than two consecutive equal words in a row. It is also guaranteed that between two such pairs there are at least two symbols.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ letter.length ≤ 250</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The number of pairs of consecutive equal words in the <code>letter</code>.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
