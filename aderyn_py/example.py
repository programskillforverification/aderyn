from aderynpy import generate_report

# generate_report("../tests/foundry-nft-f23", ".", 
#     path_includes=["../tests/foundry-nft-f23/src/F1.sol", "../tests/foundry-nft-f23/src/F2.sol"],
#     src=["../tests/no-sol-files/extra/HelloAgain.md"],
#     path_excludes=["../tests/foundry-nft-f23/src/F1.sol", "../tests/adhoc-sol-files/Counter.sol"],
# )
generate_report("../tests/contract-playground", "./report.md", 
    path_includes=["src/eth2", "src/inheritance"],
    # src=["../tests/no-sol-files/extra/HelloAgain.md"],
    # path_excludes=["../tests/foundry-nft-f23/src/F1.sol", "../tests/foundry-nft-f23/src/F2.sol"],
)