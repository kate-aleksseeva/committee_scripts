networks = [
    'arbitrum', # to be checked
    'aurora',
    'avalanche',
    'base', # to be checked
    'base-sepolia',
    'blast',
    'bsc', # to be checked
    'celo',
    'chiado',
    'gnosis-chain',
    'linea',
    'mainnet', # to be checked
    'mantle', # to be checked
    # 'mode', # is not supported by safe-api
    # 'oeth', # is not supported by safe-api
    'optimism', # to be checked
    'polygon',
    'scroll',  # to be checked
    'xlayer',
    'worldchain',
    'zksync', # to be checked
    'zkevm',
    # 'zircuit', # is not supported by safe-api
]

# checksum!
signers = [
    # LOL
    ("ajbeal", "0x5a409567bCa7459b3aC7e6E5a3F1a3C278071b71"),
    ("eboadom", "0xA39a62304d8d43B35114ad7bd1258B0E50e139b3"),
    ("michwill", "0xFe45baf0F18c207152A807c1b05926583CFE2e4b"),
    ("thedzhon", "0x59F8D74Fe49d5ebEAc069E3baf07eB4b614BD5A7"),
    ("George", "0x912e21CdA3D7012146da4Df33309d860a9eb0bEb"),
    ("kadmil", "0x9A3f38AF97b791C85c043D46a64f56f87E0283D4"),

    # EmBr
    ("psirex", "0x2a61d3ba5030Ef471C74f612962c7367ECa3a62d"),
    # ("TheDZhon", "0x59f8d74fe49d5ebeac069e3baf07eb4b614bd5a7"), - repeated
    ("kadmil", "0x6f5c9B92DC47C89155930E708fBc305b55A5519A"),
    ("ujenjt", "0xdd19274b614b5ecAcf493Bc43C380ef6B8dfB56c"),
    ("folkyatina", "0xCFfE0F3B089e46D8212408Ba061c425776E64322"),
]

ms_list = {
    '0x8772E3a2D86B9347A2688f9bc1808A6d8917760C': 'GateSeal Committee',
    '0x73b047fe6337183A454c5217241D780a932777bD': 'Emergency Brakes: Ethereum',
    '0x4Cf8fE0A4c2539F7EFDD2047d8A5D46F14613088': 'Emergency Brakes: Optimism',
    '0xfDCf209A213a0b3C403d543F87E74FCbcA11de34': 'Emergency Brakes: Arbitrum',
    '0x0F9A0e7071B7B21bc7a8514DA2cd251bc1FF0725': 'Emergency Brakes: Base',
    '0xa8579D42E34398267dE16e6eeeCdb7ED0EFF953C': 'Emergency Brakes: Mantle',
    '0x0D7F0A811978B3B62CbfF4EF6149B5909EAcfE94': 'Emergency Brakes: ZKSync',
    '0xF580753E334687C0d6b88EF563a258f048384Ee6': 'Emergency Brakes: Scroll',
    '0x244912352A639001ceCFa208cDaa7CB474c9eadE': 'Emergency Brakes: Mode',
    '0xC2b778fCc3FF311Cf1abBF4E53880277bfD14C8f': 'Emergency Brakes: Binance Smart Chain (BSC)',
    '0x9Bff79BF7226cB5C16d0Cca9c1dc60450feE560d': 'Emergency Brakes: Zircuit',
    '0xd65Fa54F8DF43064dfd8dDF223A446fc638800A9': 'Lido on Polygon',
    '0xa02FC823cCE0D016bD7e17ac684c9abAb2d6D647': 'Treasury Committee',
    '0x5181d5D56Af4f823b96FE05f062D7a09761a5a53': 'Gas Supply Committee',
    '0x17F6b2C738a63a8D3A113a228cfd0b373244633D': 'Pool Maintenance Labs Ltd.(PML)',
    '0x14CeF290c79fc84FDDfDf4129Ba335972aAc7F41': 'Lido Subgraph NFT owner',
    '0x12a43b049A7D330cB8aEAB5113032D18AE9a9030': 'LEGO Committee',
    '0x48F300bD3C52c7dA6aAbDE4B683dEB27d38B9ABb': 'Finance Ops',
    '0x98be4a407Bff0c125e25fBE9Eb1165504349c37d': 'Relay Maintenance Committee',
    '0x08637515E85A4633E23dfc7861e2A9f53af640f7': 'Simple DVT staking module committee ms',
    '0x81698f87C6482bF1ce9bFcfC0F103C4A0Adf0Af0': 'Mellow, https://research.lido.fi/t/mellow-lido-alliance-proposal/7557/29',
    '0x9437B2a8cF3b69D782a61f9814baAbc172f72003': 'Mellow admin',
    '0xA8ef4Db842D95DE72433a8b5b8FF40CB7C74C1b6': 'Liquidity Observation Lab: (Linea)',
    '0x10A19e7eE7d7F8a52822f6817de8ea18204F2e4f': 'Balancer, DAO MS, https://etherscan.io/address/0x10a19e7ee7d7f8a52822f6817de8ea18204f2e4f',
    '0x043f9687842771b3dF8852c1E9801DCAeED3f6bc': 'Balancer, Optimism DAO MS, https://optimistic.etherscan.io/tokenholdings?a=0x043f9687842771b3dF8852c1E9801DCAeED3f6bc',
    '0x58099b94e660bBe19848547F6c5d76DcA7282E45': 'https://snapshot.box/#/s:balancer.eth/proposal/0xbd2f095f693ec886a4774f928656a6552632f32ec81971b1072b569af59d91d5',
    '0x4f22C2784Cbd2B24a172566491Ee73fee1A63c2e': 'https://snapshot.box/#/s:aurafinance.eth/proposal/0x2ddfe69795e30a84572e2ccdc699e10fc33c2f5ffedff94fc019a11eaaab6176',
    '0x2a5AEcE0bb9EfFD7608213AE1745873385515c18': 'https://snapshot.box/#/s:balancer.eth/proposal/0x66e209613280ca9a15243fb414d12c447dbc6704231430a4446d0dff864b8fce',
    '0x0EFcCBb9E2C09Ea29551879bd9Da32362b32fc89': 'https://snapshot.box/#/s:aurafinance.eth/proposal/0xb9053a4cc769aee891b74d5c347943e83994f2da2335ef349f62996e5f479654',
    '0xeE071f4B516F69a1603dA393CdE8e76C40E5Be85': 'https://snapshot.box/#/s:balancer.eth/proposal/0x624eafaf87f3b718fae6b9fd6f68dc4e42ac085cb26b8b340af6fe986c62747e',
    '0x2f237e7643a3bF6Ef265dd6FCBcd26a7Cc38dbAa': 'https://snapshot.box/#/s:balancer.eth/proposal/0xb2f943325bef36af2f469e0ba70c508c836a5ddfca5a43b46fde62c5acb9e34c',
    '0xC40DCFB13651e64C8551007aa57F9260827B6462': 'https://snapshot.box/#/s:aurafinance.eth/proposal/0xc931351204972ed6cd36b72132399d5540be2472c2f312fd83f72c68f94bdea5',
    '0xaF23DC5983230E9eEAf93280e312e57539D098D0': 'https://snapshot.box/#/s:balancer.eth/proposal/0x50c144d0f8922aeeac41ed106f5852300506f87ed9ac7213c1992bcdb8710e0b',
    '0x17b11FF13e2d7bAb2648182dFD1f1cfa0E4C7cf3': 'https://snapshot.box/#/s:aurafinance.eth/proposal/0x05861ab7e4c32bd96b8a006543c8d73242df3d4f9b1c250c3cbec65bb7986621',
    '0x7A28A80DcE1733944Db5dC50dc2c5147eC993C5A': 'https://docs.prismafinance.com/governance/admin-functions/emergency-multisig',
    '0x6365812968f1112b90B5D43c25B742e03D9043f9': 'https://gov.blockswap.network/t/grant-application-allocate-incentives-for-conducting-an-educational-quiz-on-deth-and-bsn-in-the-curve-community/617',
    '0xC1C2F3eE323Ce42478c1c77BfCe09eAA5E7F72C2': 'https://www.coincarp.com/currencies/spell-token/richlist/',
    '0x9b8663d8dd926EEe821043eE957c9DE22B58B48d': 'https://snapshot.box/#/s:zunamidao.eth/proposal/0x93c3b03e0216c4825608afef29899623a6bed08b9dc6ae9bd40c279bfac29a29',
    '0x5f0DeE98360d8200b20812e174d139A1a633EDd2': 'https://ethplorer.io/ru/address/0x99d8a9c45b2eca8864373a26d1459e3dff1e17f3#',
    '0xFEB4acf3df3cDEA7399794D0869ef76A6EfAff52': 'https://taikoscan.io/address/0xfeb4acf3df3cdea7399794d0869ef76a6efaff52',
    '0x4217AA01360846A849d2A89809d450D10248B513': 'https://gov.optimism.io/t/draft-gf-phase-1-proposal-abracadabra-money-cycle-8/2918',
    '0x9d9bC38bF4A128530EA45A7d27D0Ccb9C2EbFaf6': 'https://binplorer.com/address/0xfe19f0b51438fd612f6fd59c1dbb3ea319f433ba#',
    '0x7d847c4A0151FC6e79C6042D8f5B811753f4F66e': 'https://docs.abracadabra.money/learn/tokens/tokenomics',
    '0x518385dd31289F1000fE6382b0C65df4d1Cd3bfC': 'https://docs.threshold.network/governance/dao/threshold-multisigs',
    '0xf46BB6dDA9709C49EfB918201D97F6474EAc5Aea': 'https://docs.abracadabra.money/learn/tokens/tokenomics',
    '0xa6A7020B3276e86011a33638F3CD8fe02d5E4b61': 'https://forum.arbitrum.foundation/t/proposal-request-to-match-my-donation-to-boostrap-curve-lending-on-arbitrum/22975',
    '0xae64A325027C3C14Cf6abC7818aA3B9c07F5C799': 'https://docs.abracadabra.money/learn/tokens/tokenomics',
    '0x48bfC7C0C6EBA7486797FdBb75e22A55F20cEE51': 'Lido/Melow MS, https://docs.mellow.finance/mellow-lrt-lst-primitive/security',
    '0x87D93d9B2C672bf9c9642d853a8682546a5012B5': 'Polygon MS, https://research.lido.fi/t/lido-on-l2-third-edition-polygon/4068',
    '0x3cd9F71F80AB08ea5a7Dca348B5e94BC595f26A0': 'Lido DEV MS',
}